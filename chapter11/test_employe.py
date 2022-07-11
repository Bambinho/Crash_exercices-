import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):

	def setUp(self):
		self.employee=Employee('Tiemoko','Bamba',50000)

	def test_give_default_raise(self):
		salary=self.employee.give_raise()
		self.assertEqual(salary, 50000+5000)

	def test_give_custom_raise(self):
		salary1=self.employee.annual_salary
		salary=self.employee.give_raise(200)
		self.assertEqual(salary,salary1+200)


if __name__=='__main__':

	unittest.main()

