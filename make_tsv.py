#!/usr/bin/python3
# -*-coding:utf-8 -*

# ----------------------------------------------------------
# Script Name: make_tsv.py
# Date: June 19, 2024
# Purpose: This script serves as the mapper function in a MapReduce job. It takes input text data,
#         creates a Google-compliant .tsv file with url, file size, and md5 checksum.
# Author: Stephane Berhault
# ----------------------------------------------------------



import os, hashlib, base64


PREFIX = 'https://github.com/Stekosan/merrer/books/main' # DONT scrape Gutenberg
BK_DIR = '../books/'
