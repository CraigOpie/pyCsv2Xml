#!/usr/bin/env python
"""
Names:	Team Awesome (Craig Opie)
Class: 	CENT110
File:	hw8.py

Algorithm:
1)  Take input from the user to specify the filename of the csv file.
2)  Load the infile using the user provided filename.
3)  Load the list 'lines' using the readlines() function.
4)  Close the infile after all data is read.
5)  Create a variable 'lastline' and store the last item in 'lines'.
6)  Split 'lastline' using the Tab delimiter.
7)  Create a list for hw1 grades.
8)  Create a list for hw2 grades.
9)  Create a list for exam1 grades.
10) Create a list for first names.
11) Create a list for last names.
12) Create a list for assignment weights.
13) Create a list for the 2D table.
14) Create a list for grades from the 2D table.
15) For each item in 'lastline':
    A.  Add the value to the list weights.
16) For each line in 'lines' with the exception of header information and the last line:
    A.  Split each line using the Tab delimiter.
    B.  Add the first item in 'lines' in the 'names' list.
    C.  Add the second column to 'hw1' and remove the '%'.
    D.  Add the third column to 'hw2' and remove the '%'.
    E.  Add the fourth column to 'exam1' and remove the '%'.
    F.  Add the second column in 'names' to 'firstnames'.
    G.  Add the first column in 'names' to 'lastname'.
17) Add 'hw1' to 'table'.
18) Add 'hw2' to 'table'.
19) Add 'hw3' to 'table'.
20) Create a for loop within the column:
    A.  Create a list to store 'column' information.
    B.  Create a nested for loop within the rows:
        1.  Create a variable named 'score' to get the point amount of the grade.
        2.  Add 'score' to 'column'
    C.  Add 'column' to 'grades'.
21) Take input from the user to specify the filename of the xml file.
22) Create an outfile using the user provided filename.
23) Write the xml header information to 'contents'.
24) Write the first tag '<students>' to 'contents'.
25) Create a for loop for each student in 'grades':
    A.  Write to 'contents' <student>.
    B.  Write to 'contents' <firstName> + firstnames[student] + </firstName>.
    C.  Write to 'contents' <lastName> + lastnames[student] + </lastName>.
    D.  Write to 'contents' <overall> + ("%.2f"%((sum(grades[student]))/sum(weights)*100)) + </overall.
    E.  Write to 'contents' </student>.
26) Write the xml closing tag for </students> to 'contents'.
27) Close the outfile after all writing is complete.
"""
# Ask the user for the filename that is to be read (csv file)
filename = input("Please specify the filename to open: ")

# Load the user's file, store each line into a list 'lines', and close the file
with open(filename, "r") as infile:
    lines = infile.readlines()
    infile.close()

# Load the last line from 'lines' and split based on tabs
lastline = lines[len(lines)-1]
lastline = lastline.strip().split("\t")

# Create list variables to be used
hw1 = []
hw2 = []
exam1 = []
firstnames = []
lastnames = []
weights = []
table = []
grades = []

# Append the values from the last line to 'weights'
for items in range(1,len(lastline)):
    weights.append(int(lastline[items]))

# Split the remaining lines (not including headers) and organize the values using lists
for line in range(2,len(lines)-1):
    line = lines[line].strip().split("\t")
    names = (line[0]).split(",")

    hw1.append(float(line[1].strip("%")))
    hw2.append(float(line[2].strip("%")))
    exam1.append(float(line[3].strip("%")))
    firstnames.append(names[1].strip())
    lastnames.append(names[0].strip())

# Create a 2D table using the data organized for grades
table.append(hw1)
table.append(hw2)
table.append(exam1)

# Create a new list based off of each students' performance named 'grades'
for col in range(len(table[0])):
    column = []
    for row in range(len(table)):
        score = ((table[row][col])/100*weights[row])
        column.append(score)
    grades.append(column)
# Ask the user for the filename that is going to be saved (xml file)
filename = input("Please specify a filename to save: ")

# Creates a file using the user specified filename
with open(filename, "w") as outfile:
    # Create a variable to store information for the xml file and write the header information
    outfile.write('<?xml version"1.0" ?>')
    outfile.write('\n<students>')

    # Add each student using 'firstnames', 'lastnames', and grades for the xml file
    for student in range(len(grades)):
        outfile.write('\n    <student>')
        outfile.write('\n        <firstName>' + firstnames[student] + '</firstName>')
        outfile.write('\n        <lastName>' + lastnames[student] + '</lastName>')
        outfile.write('\n        <overall>' + ("%.2f"%((sum(grades[student]))/sum(weights)*100)) + '</overall')
        outfile.write('\n    </student>')

    # Write the closing tag for the xml file
    outfile.write('\n</students>')

    # Close the outfile after all data is written
    outfile.write(contents)
