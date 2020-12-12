#!/usr/bin/python
import os
import math

fieldSize = 10

userInput = float(input())

#not necessary
while userInput >= 75.0 or userInput <= -75.0:
    print("invalid input, try again.")
    userInput = float(input("input a number between -75 and 75 "))

userInput = math.radians(userInput)
distance = fieldSize*math.tan(userInput)

print(distance, flush=True)
