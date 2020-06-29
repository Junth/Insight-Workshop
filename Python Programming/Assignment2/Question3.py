# Question 3: Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

from collections import defaultdict

paragraph = 'cat act like it played tic tac toe and dog act like it is god'.strip().split(' ')
anagrams = defaultdict(list)
for word in paragraph:
    anagrams[''.join(sorted(word))].append(word)
print((*[anagram for anagram in anagrams.values() if len(anagram) > 1]))
    
    



