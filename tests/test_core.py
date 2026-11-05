import unittest
from http_redirect_credential_lab.core import run
class DomainTests(unittest.TestCase):
 def test_stripping(self):self.assertEqual(run({})['experiments']['strip_cross_origin']['forwarded_header_names'],[])
 def test_default_observed(self):self.assertIn('authorization',run({})['experiments']['stdlib']['forwarded_header_names'])
