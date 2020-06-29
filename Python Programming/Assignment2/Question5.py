# Question 5: Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

sample_tuple = ('Junth', 'Basnet', 21)
people = []
people.append(sample_tuple)
print(people)

# [('Junth', 'Basnet', 21)]

supreme_tuple = ('Supreme', 'Thapa', 22)
sush_tuple = ('Sushmita', 'Thapa', 20)
james_tuple = ('James', 'Basnet', 15)
people = [*people, supreme_tuple, sush_tuple, james_tuple]
print(people)

# [('Junth', 'Basnet', 21), ('Supreme', 'Thapa', 22), ('Sushmita', 'Thapa', 20), ('James', 'Basnet', 15)]

print(sorted(people, key=lambda a:a[0]))
# [('James', 'Basnet', 15), ('Junth', 'Basnet', 21), ('Supreme', 'Thapa', 22), ('Sushmita', 'Thapa', 20)]

print(sorted(people, key=lambda a:a[1]))
# [('Junth', 'Basnet', 21), ('James', 'Basnet', 15), ('Supreme', 'Thapa', 22), ('Sushmita', 'Thapa', 20)]

print(sorted(people, key=lambda a:a[-1]))
# [('James', 'Basnet', 15), ('Sushmita', 'Thapa', 20), ('Junth', 'Basnet', 21), ('Supreme', 'Thapa', 22)]

print(sorted(people, key=lambda a:(a[0], a[1])))
# [('James', 'Basnet', 15), ('Junth', 'Basnet', 21), ('Supreme', 'Thapa', 22), ('Sushmita', 'Thapa', 20)]