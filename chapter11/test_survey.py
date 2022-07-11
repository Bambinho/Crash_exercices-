import unittest 
from survey import AnonymousSurvey 

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for the class Anonymous Survey"""

	def setUp(self):
		"""Creat a survey and a set of responses for use in all test methodes.
		"""
		question="What language did you first learn to speak?"
		self.my_survey=AnonymousSurvey(question)
		self.responses=['English','French','Dioula']

	def test_store_single_repomse(self):
		"""Test that a single response is stored properly"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.my_survey.responses)
	def test_store_three_response(self):

		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)

if __name__=='__main__':
	unittest.main()