def binary_search(sequence, target):
    if len(sequence) == 0:
        return False
    midpoint = len(sequence) // 2
    if sequence[midpoint] == target:
        return True
    elif target < sequence[midpoint]:
        return binary_search(sequence[:midpoint], target)
    else:
        return binary_search(sequence[midpoint+1:], target)


print(binary_search([0, 1, 2, 8, 13, 17, 19, 32, 42], 1))
print(binary_search([0, 1, 2, 8, 13, 17, 19, 32, 42], 3))