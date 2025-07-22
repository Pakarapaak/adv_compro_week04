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

#Ex4
import string_operations as so
sample_string = "hello World"
print("Original:", sample_string)
print("Reversed:", so.reverse_string(sample_string))
print("Capitalized:", so.capitalize_string(sample_string))
print("Lowercase:", so.lowercase_string(sample_string))
print("Uppercase:", so.uppercase_string(sample_string))