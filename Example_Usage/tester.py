# !/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys, io
from itertools import groupby

## Change this value
PROBLEM = ""
test_results = dict()

SOLUTION_PROGRAM = ''
CURR_DIR = ''
TEST_DATA_DIR = ''

def SETUP_ENV(input):
    global SOLUTION_PROGRAM, CURR_DIR, TEST_DATA_DIR, PROBLEM

    PROBLEM = input
    SOLUTION_PROGRAM = __import__(PROBLEM)
    CURR_DIR = os.getcwd()
    TEST_DATA_DIR = ".\\all_data\\" + PROBLEM + "\\"

## Helper Methods
def ADD_TO_DIC(dict, key, value):
    if key not in dict:
        dict[key] = value
    else:
        print("ERROR: CANNOT ADD " + key + ", " + value)

def RUN():
    return SOLUTION_PROGRAM.run()

def GET_DATA(dir):
    files = os.listdir(dir)
    groups = {key: set(value)
            for key, value in groupby(sorted(files, key = lambda e: os.path.splitext(e)[0]),
                                        key = lambda e: os.path.splitext(e)[0])}
    return groups

def OPEN_FILE(file_name):
    with open(TEST_DATA_DIR + file_name) as input:
        return input.read()


## Main Tests
def PRINT_RES():
    files = sorted(test_results, key=lambda x:test_results[x], reverse=True)

    for file in files:
        print(file + ": " + test_results[file])

## Unittest Mocking Input
import unittest
from unittest.mock import patch
from io import StringIO

class TEST(unittest.TestCase):
    PROBLEM = ''
    def test(self):

        SETUP_ENV(PROBLEM)
        TEST_DATA = GET_DATA(TEST_DATA_DIR)

        for key in TEST_DATA:
            if (len(TEST_DATA[key]) != 2):
                ADD_TO_DIC(test_results, key, "MISSING TEST FILES")
                continue
            input_str = OPEN_FILE(key + ".in")
            output_str = OPEN_FILE(key + ".out")

            inputs = str.split(input_str, "\n")

            with patch('builtins.input', side_effect=inputs):
                # Redirect stdout to capture print statements
                captured_output = StringIO()
                sys.stdout = captured_output

                # Call the function
                RUN()

                # Reset redirect.
                sys.stdout = sys.__stdout__

                # Get the printed output
                output = captured_output.getvalue()
                output = str.strip(output)+"\n"
                output_str = str.strip(output_str)+"\n"

                # Assert the output
                self.assertEqual(output, output_str)

if __name__ == '__main__':
    PROBLEM = sys.argv.pop()
    TEST.PROBLEM = PROBLEM
    unittest.main()