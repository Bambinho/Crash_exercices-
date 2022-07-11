import unittest 
from city_function import get_formatted_place

class PlaceTestCase(unittest.TestCase):
	""" Test the function city_function """

	def test_place_function(self):
		""" does place like santiago chilie works"""
		place=get_formatted_place('santiago','chilie')
		self.assertEqual(place,'Santiago, Chilie')

	def test_place_population_function(self):
		"""does places like santiago chile 5_000_000 works"""
		place=get_formatted_place('santiago','chilie',5000000)
		self.assertEqual(place,"Santiago, Chilie- population 5000000")


if __name__=='__main__':
	unittest.main()

