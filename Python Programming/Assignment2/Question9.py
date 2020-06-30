# Question 9: Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.


def binary_search(seq, num):
    low = 0
    high = len(seq) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if seq[mid] > num:
            high = mid - 1
        elif num > seq[mid]:
            low = mid + 1
        else:
            return mid
    return -1


seq = [4, 10, 20, 15, 50, 100, 70, 60]
seq.sort()
print(seq)
# [4, 10, 15, 20, 50, 60, 70, 100]

print(binary_search(seq, 50))
# 4

print(binary_search(seq, 120))
# -1
