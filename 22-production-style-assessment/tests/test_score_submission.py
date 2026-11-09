import csv
import tempfile
import unittest
from pathlib import Path

from score_submission import ROOT, load, score


class ScoreSubmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gold_rows = list(csv.DictReader((ROOT / "gold-standard.csv").open(encoding="utf-8", newline="")))

    def write_candidate(self, rows):
        handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", suffix=".csv", delete=False)
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        fields = ["task_id", "intent", "priority", "action_required", "confidence", "rationale", "started_at_utc", "completed_at_utc"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
        handle.close()
        return Path(handle.name)

    def candidate_rows(self):
        rows = []
        for gold in self.gold_rows:
            rows.append({
                "task_id": gold["task_id"],
                "intent": gold["intent"],
                "priority": gold["priority"],
                "action_required": gold["action_required"],
                "confidence": "high",
                "rationale": "Evidence-grounded test rationale",
                "started_at_utc": "2026-11-09T10:00:00Z",
                "completed_at_utc": "2026-11-09T10:30:00Z",
            })
        return rows

    def test_reference_labels_score_and_throughput(self):
        result = score(self.write_candidate(self.candidate_rows()))
        self.assertEqual(result["records"], 30)
        self.assertEqual(result["exact_match_pct"], 100.0)
        self.assertEqual(result["elapsed_minutes"], 30.0)
        self.assertEqual(result["records_per_hour"], 60.0)
        self.assertEqual(result["label_quality_issues"], [])

    def test_missing_label_is_flagged_and_not_exact_match(self):
        rows = self.candidate_rows()
        rows[0]["intent"] = ""
        result = score(self.write_candidate(rows))
        self.assertEqual(result["exact_match"], 29)
        self.assertTrue(any(item["task_id"] == "T001" and item["issue"] == "missing" for item in result["label_quality_issues"]))

    def test_inconsistent_timestamps_prevent_throughput(self):
        rows = self.candidate_rows()
        rows[1]["started_at_utc"] = "2026-11-09T10:01:00Z"
        result = score(self.write_candidate(rows))
        self.assertEqual(result["throughput"], "not calculated")
        self.assertTrue(any("consistent timestamp" in item for item in result["timing_errors"]))

    def test_duplicate_task_ids_rejected(self):
        rows = self.candidate_rows()
        rows[1]["task_id"] = rows[0]["task_id"]
        with self.assertRaisesRegex(ValueError, "Duplicate task_id"):
            score(self.write_candidate(rows))

    def test_missing_task_id_rejected(self):
        rows = self.candidate_rows()
        rows.pop()
        with self.assertRaisesRegex(ValueError, "Task ID mismatch"):
            score(self.write_candidate(rows))


if __name__ == "__main__":
    unittest.main()
