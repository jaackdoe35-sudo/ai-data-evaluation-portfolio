"""Deterministic, synthetic stress test for the portfolio's four QA utilities."""
import csv
import hashlib
import importlib.util
import json
import platform
import random
import sys
import tempfile
import time
import tracemalloc
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCALE_SIZES = (10_000, 50_000, 100_000)
SEED = 20261103
INTENTS = ("account_access", "profile_update", "card_delivery", "transfer_status")
SENTIMENTS = ("neutral", "negative", "positive")
URGENCIES = ("routine", "standard", "elevated", "urgent")
DIMENSIONS = ("factuality", "instruction_following", "completeness", "clarity", "safety_judgment")
ANNOTATION_FIELDS = (
    "record_id", "message_text", "primary_intent", "secondary_intent", "sentiment",
    "urgency", "pii_types", "pii_span_to_redact", "clarification_flag",
    "annotation_rationale",
)
SCORE_FIELDS = ("id", *DIMENSIONS, "issue_severity")


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def measured(label, operation):
    tracemalloc.start()
    started = time.perf_counter()
    result = operation()
    elapsed = time.perf_counter() - started
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, {"operation": label, "elapsed_seconds": round(elapsed, 4),
                    "python_tracemalloc_peak_mib": round(peak / (1024 * 1024), 3)}


def write_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def annotation_rows(count):
    rng = random.Random(SEED)
    for index in range(1, count + 1):
        yield {
            "record_id": f"ST{index:05d}",
            "message_text": f"Synthetic support request {index}: please review my {rng.choice(('account', 'card', 'transfer'))} query. " + ("Unicode test: café — 東京. " if index % 97 == 0 else ""),
            "primary_intent": rng.choice(INTENTS),
            "secondary_intent": "",
            "sentiment": rng.choice(SENTIMENTS),
            "urgency": rng.choice(URGENCIES),
            "pii_types": "none",
            "pii_span_to_redact": "",
            "clarification_flag": "no",
            "annotation_rationale": "Synthetic benchmark row; label assigned by deterministic generator.",
        }


def score_rows(count):
    rng = random.Random(SEED + 1)
    for index in range(1, count + 1):
        row = {"id": f"EV{index:05d}", "issue_severity": rng.choice(("None", "Minor", "Major"))}
        row.update({dimension: str(rng.randint(1, 5)) for dimension in DIMENSIONS})
        yield row


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    validator = load_module("portfolio_validator", "10-annotation-csv-validator/validator.py")
    consistency = load_module("portfolio_consistency", "11-annotation-consistency-checker/consistency_checker.py")
    calculator = load_module("portfolio_score", "12-ai-response-score-calculator/score_calculator.py")
    dashboard = load_module("portfolio_dashboard", "13-annotation-qa-dashboard/qa_dashboard.py")

    scale_results = []
    with tempfile.TemporaryDirectory(prefix="annotation-qa-scale-") as temporary:
        work = Path(temporary)
        for count in SCALE_SIZES:
            annotation_path = work / f"annotations_{count}.csv"
            score_path = work / f"evaluations_{count}.csv"
            write_csv(annotation_path, ANNOTATION_FIELDS, annotation_rows(count))
            write_csv(score_path, SCORE_FIELDS, score_rows(count))
            annotation_hash_before = sha256(annotation_path)
            score_hash_before = sha256(score_path)
            measurements = []

            errors, metric = measured(
                f"validator.validate_file ({count:,} annotation rows)",
                lambda: validator.validate_file(annotation_path),
            )
            measurements.append(metric)
            assert errors == [], f"Validator rejected {count:,}-row clean dataset: {errors[:5]}"

            flags, metric = measured(
                f"consistency.check_file ({count:,} annotation rows)",
                lambda: consistency.check_file(annotation_path),
            )
            measurements.append(metric)
            assert flags == [], f"Consistency checker flagged {count:,}-row clean dataset: {flags[:5]}"

            inspected, metric = measured(
                f"dashboard.inspect ({count:,} annotation rows)",
                lambda: _inspect_file(dashboard, annotation_path),
            )
            measurements.append(metric)
            assert len(inspected["rows"]) == count, f"Dashboard loaded {len(inspected['rows'])}/{count} rows"
            assert inspected["issues"] == [], f"Dashboard found unexpected issues: {inspected['issues'][:5]}"

            def calculate():
                with score_path.open(encoding="utf-8-sig", newline="") as handle:
                    reader = csv.DictReader(handle)
                    records = calculator.analyze_rows(reader.fieldnames, reader)
                report = calculator.render_report(records)
                return records, report

            (records, score_report), metric = measured(
                f"score_calculator.analyze_rows + render_report ({count:,} evaluations)",
                calculate,
            )
            measurements.append(metric)
            assert len(records) == count, f"Score calculator processed {len(records)}/{count} rows"
            assert f"Evaluated responses: {count}" in score_report

            repeat_annotation = work / f"annotations_{count}_repeat.csv"
            repeat_scores = work / f"evaluations_{count}_repeat.csv"
            write_csv(repeat_annotation, ANNOTATION_FIELDS, annotation_rows(count))
            write_csv(repeat_scores, SCORE_FIELDS, score_rows(count))
            deterministic = (
                sha256(annotation_path) == sha256(repeat_annotation)
                and sha256(score_path) == sha256(repeat_scores)
            )
            assert deterministic, f"{count:,}-row generation was not deterministic"

            unchanged = (
                annotation_hash_before == sha256(annotation_path)
                and score_hash_before == sha256(score_path)
            )
            assert unchanged, f"A tool modified a {count:,}-row input file"

            scale_results.append({
                "row_count": count,
                "evaluation_count": count,
                "all_tools_processed_expected_rows": True,
                "all_tools_reported_no_unexpected_findings": True,
                "deterministic_generation": deterministic,
                "input_files_unchanged": unchanged,
                "measurements": measurements,
            })

        # Preserve the negative-input checks from the initial 10,000-row run.
        negative_checks = []
        duplicate_header_errors = validator.validate_rows(["record_id", "record_id"], [])
        assert any("duplicate column" in item.lower() for item in duplicate_header_errors)
        negative_checks.append("validator rejects duplicate headers")

        bad_utf8 = work / "invalid_utf8.csv"
        bad_utf8.write_bytes(b"\xff\xfe\xfa")
        assert validator.validate_file(bad_utf8)
        negative_checks.append("validator reports undecodable input")

        missing_file = _write_text(work / "missing.csv", "message_text\nhello\n")
        missing_columns = consistency.check_file(missing_file)
        assert any("Missing required column" in item for item in missing_columns)
        negative_checks.append("consistency checker reports missing required columns")

        try:
            dashboard.inspect(["record_id", "record_id"], [])
        except ValueError as exc:
            assert "duplicate column" in str(exc).lower()
        else:
            raise AssertionError("Dashboard accepted duplicate headers")
        negative_checks.append("dashboard rejects duplicate headers")

        summary = {
            "status": "PASS",
            "scale_sizes": list(SCALE_SIZES),
            "seed": SEED,
            "scale_results": scale_results,
            "negative_checks_passed": negative_checks,
            "environment": {
                "python": sys.version.split()[0],
                "platform": platform.platform(),
                "implementation": platform.python_implementation(),
            },
            "measurement_note": (
                "Elapsed time is wall-clock time for the measured Python call. "
                "Memory is tracemalloc-tracked Python allocation peak, not process RSS "
                "or total system memory. Results are specific to this runner. "
                "Scale runs are sequential and do not test concurrency or sustained load."
            ),
        }
        output = ROOT / "16-annotation-qa-stress-test" / "scale-test-results.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(summary, indent=2))


def _inspect_file(module, path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return module.inspect(reader.fieldnames, reader)


def _write_text(path, content):
    path.write_text(content, encoding="utf-8")
    return path



if __name__ == "__main__":
    main()
