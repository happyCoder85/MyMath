"""
Description: Test application for MyMath class
Author: Jonathan Spurling
Section Number: ADEV-3005(251409)
Date Created: February 18, 2024

Updates: none
"""
from my_math import MyMath

num_list = MyMath()

while True:
    number = input("Enter a number or type done: ")

    if(number == "done"):
        break
    else:
        num_list.num_list.append(int(number))


average = MyMath.calculate_average(num_list)
std_deviation = MyMath.calculate_standard_deviation(num_list)

print(f"The average of {num_list.num_list} is {average} and the standard deviation is {std_deviation}.")

