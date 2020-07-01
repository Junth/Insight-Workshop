# Question 20: Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]


class ZeroSum:
    def zero_sum_triplets(self, array):
        triplets = []
        n = len(array)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (array[i] + array[j] + array[k] == 0):
                        triplets.append([array[i], array[j], array[k]]) 
        return triplets

sample = ZeroSum()
print(sample.zero_sum_triplets([-25, -10, -7, -3, 2, 4, 8, 10]))
# [[-10, 2, 8], [-7, -3, 10]]
        
        