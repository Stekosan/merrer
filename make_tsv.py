#!/usr/bin/python3
# -*-coding:utf-8 -*

# ----------------------------------------------------------
# Script Name: make_tsv.py
# Date: June 19, 2024
# Purpose: This script serves as the mapper . It takes input text data,
#         creates a Google-compliant .tsv file with url, file size, and md5 checksum.
# Author: Stephane Berhault
# ref doc : https://cloud.google.com/storage-transfer/docs/create-url-list?hl=en
# ----------------------------------------------------------



import os
import hashlib
import base64

# Constants
PREFIX = 'https://github.com/Stekosan/merrer/tree/main/'
BK_DIR = '../books/'

def get_file_info(file_path):
        # returns the file size and its MD5 checksum in base64 encoding.
        file_size = os.path.getsize(file_path)
    
    # Calculate MD5 checksum
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    
    md5_checksum = base64.b64encode(md5_hash.digest()).decode('utf-8')
    
    return file_size, md5_checksum

def create_tsv_file():
    # creates a TSV file containing the URL, file size, and MD5 checksum
    for each .txt file in the BK_DIR.
    
    tsv_filename = 'books_info.tsv'
    
    with open(tsv_filename, 'w') as tsv_file:
        # Write header
        tsv_file.write("TsvHttpData-1.0\n")
        
        # Iterate through the files in the directory
        for filename in os.listdir(BK_DIR):
            if filename.endswith('.txt'):
                file_path = os.path.join(BK_DIR, filename)
                
                if os.path.isfile(file_path):
                    file_size, md5_checksum = get_file_info(file_path)
                    
                    # Write the file information in TSV format
                    file_url = PREFIX + filename
                    tsv_file.write(f"{file_url}\t{file_size}\t{md5_checksum}\n")
    
    print(f"TSV file '{tsv_filename}' created successfully.")

if __name__ == '__main__':
    create_tsv_file()
