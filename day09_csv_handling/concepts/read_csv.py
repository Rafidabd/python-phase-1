"""
CSV=Comma Seperated Values
Basically-*A table stored as text,not a file with commas
string → lines → split values
[ CSV FILE ]
     ↓
csv.reader / DictReader
     ↓
Python rows (list or dict)
     ↓
Process / validate / transform
     ↓
csv.writer / DictWriter
     ↓
[ NEW CSV FILE ]





"""

import csv

with open("day09_csv_handling/sample.csv","r") as file: 
    csv_reader=csv.reader(file) #csv reader is an iterator
    for line in csv_reader:
        print(line)    ##We need to iterate..this will provide a list.each line is a list
        print(line[2])   ##if we need to print a specifically
 
    #if we want to skip the header line:
    next(csv_reader)
    for line in csv_reader:
        print(line)
    