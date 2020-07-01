# Question 14: Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22},
#  {'name': 'John', 'address': '54 Love Ave', 'age': 21}]

import csv

csvfile = open('file.csv','r', newline='')
obj = csv.DictReader(csvfile)
print(obj.fieldnames)
# ['name', 'address', 'age']

ordered_dict = [row for row in obj]
print(ordered_dict)
# [OrderedDict([('name', 'George'), ('address', '4312 Abbey Road'), ('age', '22')]),
#  OrderedDict([('name', 'John'), ('address', '54 Love Ave'), ('age', '21')])]

print([dict(row) for row in ordered_dict])
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'},
#  {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]