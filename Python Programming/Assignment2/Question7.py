# Question 7: Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

list_tuple = [('Supreme', 'Thapa', 22),
              ('Sushmita', 'Thapa', 20),
              ('James', 'Basnet', 15),
              ('Clementine', 'Karki', None)]

age = [age for *name, age in list_tuple if age != None]
avg_age = sum(age) // len(age)

result = [{first + ' ' + last : 'old'} if age > avg_age
          else {first + ' ' + last : 'young'}
          for first, last, age in list_tuple if age != None]

print(result)
# [{'Supreme Thapa': 'old'},
# {'Sushmita Thapa': 'old'},
# {'James Basnet': 'young'}]



