#!/usr/bin/python
import os
import math

def sumPalindrome(number):
    #implement
    return 0


def generatePalindrome(number):
    lower = 1

    palindrome = list("0")

    k = 0
    while k < 2:
        j = 0
        while j < 10:    #generate next outer number
            i = 0
            while i < 10:   #generate inner number

                palindrome.pop(0)
                palindrome.insert(0, i)
                i += 1
                if j > 0:
                    print(str(palindrome) + str(palindrome)[::-1])
                else:
                    print(str(palindrome))

            if len(palindrome) == j:    # set j 1 higher for the outerloop
                palindrome.pop(j)
            palindrome.insert(k, j)
            j += 1
        k += 1

def main():
    # input
    # get a number
    # make it balanced
    # calculate sum
    # output
    Userinput = int(input())
    generatePalindrome(Userinput)


if __name__ == "__main__":
        main()