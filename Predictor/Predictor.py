#!/usr/bin/python3

import sqlite3
import sys

con = None
cursor = None

def initiateDB(fileName):
    try:
        con = sqlite3.connect(fileName)
    except sqlite3.Error:
        raise Exception("Could not connect to database")

def getWords(PrevWord):
    con = sqlite3.connect(sys.argv[1])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Completions WHERE PrevWord=? ORDER BY Weight DESC", (PrevWord,))
    return cursor

#Hold on to your butts
initiateDB(sys.argv[1])
while True:
    textInput = input("Enter previous word: ")
    words = getWords(textInput)
    a = 0
    while a < 10:
        row = words.fetchone()

        if row == None:
            break
        
        print(row[1])
        a+=1
