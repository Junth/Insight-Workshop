def linear_search(sequence, target):
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


print(linear_search([0, 5, 7, 10, 15], 5))
print(linear_search([0, 5, 7, 10, 15], 15))
print(linear_search([0, 5, 7, 10, 15], 20))