#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#We provide two files for this assignment. One is a sample file where we give
#you the sum for your testing and the other is the actual data you need to
#process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt
#(There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_623885.txt
#(There are 95 values and the sum ends with 897)

#Data Format
#The file contains much of the text from the introduction of the textbook except
#that random numbers are inserted throughout the text. Here is a sample of the
#output you might see:

#The sum for the sample text above is 27486. The numbers can appear anywhere in
#the line. There can be any number of numbers in each line (including none).

import re
fname = input("Enter file:")
fhand = open(fname)

numlist = 0

for line in fhand:
    numlist = numlist + sum(map(int,re.findall('[0-9]+',line)))

print(numlist)
