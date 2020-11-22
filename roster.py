# TODO
from sys import argv, exit
from cs50 import SQL
import sqlite3

if len(argv) != 2:
    print("error")
    exit()

db = SQL("sqlite:///students.db")

house = argv[1]

database = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last;", house)

for row in database:
    print(row['first'], end=" ")
    if row['middle'] != None:
        print(row['middle'], end=" ")
    print(row['last'], end=",")
    print(" born", row['birth'])
