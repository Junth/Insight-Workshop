def bubble_sort(collection):
    n = len(collection)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
    return collection


print(bubble_sort([0, 5, 2, 3, 2]))