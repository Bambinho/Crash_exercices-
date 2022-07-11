import unittest
import python_repos as pr
class TestCase(unittest.TestCase):
		url='https://api.github.com/search/repositories?q=language:python&sort=stars'
		headers={'Accept':'application/vnd.github.v3+json'}
		r=pr.open_api(url,headers)
		def test_python_repos(self):
			self.assertEqual(self.r.status_code, 200)
		def test_count(self):
			self.assertGreater(9039426,self.r.json()['total_count'])
		def  test_item_count(self):
			self.assertEqual(len(self.r.json()['items']), 30)




if __name__=='__main__':
	unittest.main()