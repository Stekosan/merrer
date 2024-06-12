#!/usr/bin/python3
# -*-coding:utf-8 -*

# ---------------------------------------------------
# Script Name: reducer.py
# Date: June 12, 2024
# Purpose: This script serves as the reducer function in a MapReduce job. It takes the output
#          from the mapper function (key-value pairs in the format (word, 1)), aggregates the
#         counts for each word, and outputs the word-count pairs in the format 'word count'.
# Author: Stephane Berhault
# ---------------------------------------------------

from operator import itemgetter
import sys

word_counts = {}

# Read input from stdin
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
        word_counts[word] = word_counts.get(word, 0) + count
    except ValueError:
        continue

# Sort word-count pairs by word in alphabetical order
sorted_word_counts = sorted(word_counts.items(), key=itemgetter(0))

# Print word-count pairs in the desired format
for word, count in sorted_word_counts:
    print(f"{word} {count}")
