def insertion_sort(collection):
    for i in range(1, len(collection)):
        key = collection[i]
        j = i - 1
        while j >= 0 and key < collection[j]:
            collection[j+1] = collection[j]
            j -= 1
        collection[j+1] = key
    return collection
    
    
print(insertion_sort([-5, -2, -10, 10, 5, 20, 100, 2]))