
class Employee:

	def __init__(self, first,last, salary):
		self.first_name=first
		self.last_name=last
		self.annual_salary=salary

	def give_raise(self,value=5000):
		self.annual_salary+=value
		#print(f"Your new salary is {self.annual_salary}")
		return self.annual_salary


# employe=Employee('Tiemoko','Bamba',50000)
# employe.give_raise()
# employe.give_raise(2000)


