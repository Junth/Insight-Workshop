def interpolation_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        if sorted_collection[left] == sorted_collection[right]:
            if sorted_collection[left] == item:
                return left
            else:
                return None

        pos = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left]
        )

        if pos < 0 or pos >= len(sorted_collection):
            return None

        if sorted_collection[pos] == item:
            return pos
        elif sorted_collection[pos] < item:
            left = pos + 1
        else:
            right = pos - 1
    return None


print(interpolation_search([0, 1, 2, 8, 13, 17, 19, 32, 42], 42))
print(interpolation_search([0, 1, 2, 8, 13, 17, 19, 32, 42], 100))