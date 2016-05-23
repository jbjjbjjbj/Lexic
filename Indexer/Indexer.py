#!/usr/bin/python3

import sys
import os.path
import sqlite3
import mimetypes


# Try and catch any wrong input in arguments
for argument in sys.argv:
    if not os.path.isfile(argument):
        raise Exception("File " + argument + " does not exist")
    if mimetypes.guess_type(os.path.abspath(argument)) == 'text/plain':
        raise Exception("File " + argument + " is not a plain text file")

