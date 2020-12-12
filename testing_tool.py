#!/usr/bin/env python3
#
# Testing tool for the Guessing Game problem
#
# Usage:
#
#   python3 testing_tool.py -f inputfile <program invocation>
#
# Use the -f parameter to specify the input file, e.g. 1.in.
# The input file should contain a single lines containing an integer between 1 and 1000 inclusive: the answer.
#

# You can compile and run your solution as follows.
# - You may have to replace 'python3' by just 'python'.
# - On Windows, you may have to to replace '/' by '\'.

# C++:
#   g++ solution.cpp
#   python3 testing_tool.py -f 1.in ./a.out

# Java
#   javac solution.java
#   python3 testing_tool.py -f 1.in java solution

# Python3
#   python3 testing_tool.py -f 1.in python3 ./solution.py


# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
#
# The tool attempts to detect and report common errors, but it is not an
# exhaustive test. It is not guaranteed that a program that passes this testing
# tool will be accepted.
#


import argparse
import subprocess
import traceback

import sys


def write(p, line):
    assert p.poll() is None, 'Program terminated early'
    print('Write: {}'.format(line), flush=True)
    p.stdin.write('{}\n'.format(line))
    p.stdin.flush()


def read(p):
    assert p.poll() is None, 'Program terminated early'
    line = p.stdout.readline().strip()
    assert line != '', 'Read empty line or closed output pipe'
    print('Read: {}'.format(line), flush=True)
    return line


parser = argparse.ArgumentParser(description='Testing tool for problem Guessing Game.')
parser.add_argument('-f', dest='inputfile', metavar='inputfile', default=None, type=argparse.FileType('r'),
                    required=True, help='The input file to use.')
parser.add_argument('program', nargs='+', help='Invocation of your solution')

args = parser.parse_args()

answer = None
with args.inputfile as f:
    lines = f.readlines()
    assert len(lines) > 0
    answer = int(lines[0])
    assert 1 <= answer and answer <= 1000

assert answer is not None

with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                      universal_newlines=True) as p:
    try:
        while True:
            guess = int(read(p))
            if answer == guess:
                write(p, "That is correct!")
                break
            if answer > guess:
                write(p, "Your guess is too low.")
            if answer < guess:
                write(p, "Your guess is too high.")

        assert p.stdout.readline() == '', 'Your submission printed extra data after finding solution'
        assert p.wait() == 0, 'Your submission did not exit cleanly after finishing'

        sys.stdout.write('\nSuccess.\n'.format(p.wait()))
    except:
        print()
        traceback.print_exc()
        print()
        try:
            p.wait(timeout=2)
        except subprocess.TimeoutExpired:
            print('Killing your submission after 2 second timeout.')
            p.kill()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write('Exit code: {}\n'.format(p.wait()))
        sys.stdout.flush()
