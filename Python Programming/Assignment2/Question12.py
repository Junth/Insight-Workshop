# Question 12: Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.


is_palindrome = lambda word: word == word[::-1]
print(is_palindrome('racecar'))
# True
print(is_palindrome('word'))
# False