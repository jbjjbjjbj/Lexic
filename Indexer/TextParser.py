#!/usr/bin/python3

import DatabaseHelper

def parse(file_url):
    DatabaseHelper.initiateDB()
    with open(file_url, 'r') as f:
        for line in f:
            prevWord = ""
            for word in line.split():
                DatabaseHelper.addToDatabase(prevWord, word)
                prevWord = word
