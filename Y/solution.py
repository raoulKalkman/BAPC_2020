#!/usr/bin/python
import os
import math

fieldSize = 10

if __name__ == '__main__':
    userInput = float(input("input a number between -75 and 75 "))

    while userInput > 75.0 or userInput < -75.0:
        print("invalid input, try again.")
        userInput = float(input("input a number between -75 and 75 "))

    distance = fieldSize*math.tan(userInput)

    print("userInput: ", userInput)
    print("height of ball is: ", distance)