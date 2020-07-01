# Question 13: Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
    
# =============================================================================
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21
# =============================================================================

import csv


def write_CSV(filename, list_tuple):
    csv_file = open(filename, mode='w', newline='')
    header = ('name', 'address', 'age')
    list_tuple = [header, *list_tuple]
    obj = csv.writer(csv_file)
    obj.writerows(list_tuple)
    csv_file.close()
    
    
list_tuple = [('George', '4312 Abbey Road', 22),
              ('John', '54 Love Ave', 21)]
write_CSV('file.csv',list_tuple)

# Read CSV file
csvfile=open('file.csv','r', newline='')
obj=csv.reader(csvfile)

print([row for row in obj])
# [['name', 'address', 'age'],
#  ['George', '4312 Abbey Road', '22'],
#  ['John', '54 Love Ave', '21']]




