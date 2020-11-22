# TODO
from sys import argv, exit
import csv
from cs50 import SQL

if len(argv) != 2:
    print("Error")
    exit()

db = SQL("sqlite:///students.db")

with open(argv[1], "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        full_name = row["name"].split()
        value = None
        if len(full_name) == 2:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                    full_name[0], value, full_name[1], row["house"], row["birth"])

        else:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                    full_name[0], full_name[1], full_name[2], row["house"], row["birth"])
