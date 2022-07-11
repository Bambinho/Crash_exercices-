import unittest
import hn_submissions
class TestCase(unittest.TestCase):

	def test_hn_submission(self):
		r=open_api(19157034)
		sef.assertEqual(r.status_code, 20)