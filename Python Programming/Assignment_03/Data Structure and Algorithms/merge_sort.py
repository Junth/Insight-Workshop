def merge(left, right):
    i = j = 0
    final = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
    final += left[i:]
    final += right[j:]

    return final


def merge_sort(collection):
    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


print(merge_sort([-5, -2, -10, 10, 5, 20, 100, 2]))