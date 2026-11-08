import unittest
from validate_pack import validate

class AnnotationPackTests(unittest.TestCase):
 def test_pack_is_structurally_valid(self):
  self.assertEqual(validate(),[])
if __name__=="__main__":unittest.main()
