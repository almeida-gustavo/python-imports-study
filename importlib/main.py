# Importing module
import importlib
# import flask


import module

print("Before Dynamic import")

my_other_module = importlib.import_module("module")

print("The name of the module is: ",module.__name__)

module.main()




print("--------Flask section--------")
my_module = importlib.import_module("flask")
print(my_module.__name__)
print(my_module.__doc__)
print(dir(my_module))
