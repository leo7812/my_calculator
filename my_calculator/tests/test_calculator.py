
import unittest
from calculator.basic_operations import *
from calculator.advanced_operations import *
from calculator.logarithms import *
from calculator.statistics import *
from calculator.trigonometry import *

print("Addition: ", add(10,5))
print("Subtract: ", subtract(10,5))
print("multiply: ", mulitply(10,5))
print("divide: ", divide(10,5))

print("power: ", power(10,2))
print("square root: ", square_root(49))
print("factorial: ", factorial(10,2))

print("sine: ", sine(45))
print("cosine: ", cosine(45))
print("tangent: ", tangent(45))

print("log base : ", log_base(10,2))
print("natural log : ", natural_log(10))
print("exponential : ", exponential(10))

print("log base : ", log_base(10,2))

list = [1,2,4,6,3,5,5,5]

print("example list: ", list)
print("mean : ", mean(list))
print("median : ", median(list))
print("mode : ", mode(list))
print("standard deviation : ", standard_deviation(list))


