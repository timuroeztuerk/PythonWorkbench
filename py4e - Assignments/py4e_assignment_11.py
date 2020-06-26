#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+'
#and then converting the extracted strings to integers and summing up the integers.

import re
file = open("regex_sum_713679.txt")
total = 0
for line in file:
    found = re.findall('[0-9]+', line)
    for i in found:
        total = total + int(i)
print(total)
