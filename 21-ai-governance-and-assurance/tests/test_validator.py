import unittest
from validator import validate
class GovernanceStructureTests(unittest.TestCase):
    def test_current_artifacts_are_structurally_valid(self):
        self.assertEqual(validate(),[])
if __name__=="__main__": unittest.main()
