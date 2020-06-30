# Question 8: Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

# Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(3))
# True

print(is_prime(4))
# False

print(is_prime(2))
# True