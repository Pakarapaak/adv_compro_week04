""" #Ex2
import calculator
print(calculator.add(100,69))
print(calculator.subtrack(100,69))
print(calculator.multiply(100,69))
print(calculator.divide(100,69)) """

""" #Ex3
import lambda_calculator
print(lambda_calculator.add(100,69))
print(lambda_calculator.subtrack(100,69))
print(lambda_calculator.multiply(100,69))
print(lambda_calculator.divide(100,69)) """

""" #Ex4
import string_operations as so
sample_string = "hello World"
print("Original:", sample_string)
print("Reversed:", so.reverse_string(sample_string))
print("Capitalized:", so.capitalize_string(sample_string))
print("Lowercase:", so.lowercase_string(sample_string))
print("Uppercase:", so.uppercase_string(sample_string)) """

#Ex5
# Importing modules from the utilities package
from utilities.calculator import add as add_def, subtract as subtract_def, multiply as multiply_def, divide as divide_def
from utilities.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

# Sample inputs and printing results using calculator.py
print("Using calculator.py:")
print("Addition:", add_def(10, 5))
print("Subtraction:", subtract_def(10, 5))
print("Multiplication:", multiply_def(10, 5))
print("Division:", divide_def(10, 5))

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))