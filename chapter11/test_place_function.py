import unittest 
from city_function import get_formatted_place

class PlaceTestCase(unittest.TestCase):

	def test_place_function(self):
		""" Does places like Santiago, Chilie work"""
		place=get_formatted_place('santiago','chilie')
		self.assertEqual(place,"Santiago, Chilie")


if __name__=='__main__':
	unittest.main()


