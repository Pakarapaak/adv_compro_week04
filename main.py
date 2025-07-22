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

""" #Ex5
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
print("Using string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string)) """

""" #Ex6
grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = list(map(lambda x: x*1.05, filter(lambda X: X>=60, grades)))
print(passed_with_bonus) """

""" #Ex7
children = [{"name": "Alice", "age": 2, "height": 95}, 
            {"name": "Bob", "age": 4, "height": 105}, 
            {"name":"Charlie", "age": 3, "height": 110}, 
            {"name": "David", "age": 5, "height": 102}, 
            {"name": "Eve", "age": 6, "height": 99}]
eligible_children = [child for child in children if child["age"]>3 and child["height"]>100 ]
print(eligible_children) """

""" #Ex8
children = [{"name": "Alice", "age": 2, "height": 95}, 
            {"name": "Bob", "age": 4, "height": 105}, 
            {"name":"Charlie", "age": 3, "height": 110}, 
            {"name": "David", "age": 5, "height": 102}, 
            {"name": "Eve", "age": 6, "height": 99}]
criteria = lambda child: child["age"] > 3 and child["height"]>100
eligible_children = [child for child in children if criteria(child)]
print(eligible_children) """

""" #Ex8 without criteria
children = [{"name": "Alice", "age": 2, "height": 95}, 
            {"name": "Bob", "age": 4, "height": 105}, 
            {"name":"Charlie", "age": 3, "height": 110}, 
            {"name": "David", "age": 5, "height": 102}, 
            {"name": "Eve", "age": 6, "height": 99}]
eligible_children = list(filter(lambda child: child["age"] > 3 and child["height"]>100, children))
print(eligible_children) """
