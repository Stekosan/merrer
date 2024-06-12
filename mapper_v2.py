#!/usr/bin/python3
# -*-coding:utf-8 -*

# ----------------------------------------------------------
# Script Name: mapper.py
# Date: June 12, 2024
# Purpose: This script serves as the mapper function in a MapReduce job. It takes input text data,
#         extracts individual words, and outputs key-value pairs in the format (word, 1).
#         This output is then consumed by the reducer function.
# Author: Stephane Berhault
# ----------------------------------------------------------

import sys # import sys module for variable and function
import re # import re module for regex

# Define a regular expression pattern to extract words
pattern = r'\b[a-zA-Z]+\b' # match string with upper and lower letter in input text

for line in sys.stdin:
    line = line.strip()
    words = re.findall(pattern, line)
    for word in words:
        print('%s\t%s' % (word, 1))
