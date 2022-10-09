"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def findMedian(numbers):
    median=0
    if len(numbers) % 2 !=0:
        # if numbers has odd number of values
        middleValue = math.floor(len(numbers) / 2)
        median = numbers[middleValue]
    else:
        middleValue1 = math.floor(len(numbers) / 2)
        middleValue2 = middleValue1 -1
        middleSum = (numbers[middleValue1]) + (numbers[middleValue2])
        median = numbers[middleSum / 2]
    return median
    
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        # passing in sorted list
        numbers.sort()
        median = findMedian(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
