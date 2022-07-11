#from car import Car, ElectricCar 
from car import Car 
from electric_car  import ElectricCar as EC

my_beetle=Car('Volgwagen','beetle',2019)

print(my_beetle.get_descriptive_name())

my_tesla=EC('tesla','model s',2019)

print(my_tesla.get_descriptive_name())