def quick_sort(collection):
    if len(collection) <= 1:
        return collection
    else:
        pivot = collection.pop()
        greater_than_pivot = []
        lesser_than_pivot = []
        for element in collection:
            if element > pivot:
                greater_than_pivot.append(element)
            else:
                lesser_than_pivot.append(element)
        return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


print(quick_sort([-2, -10, -5, 100, 10, 5, 2, 20]))