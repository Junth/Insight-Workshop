# Question 19: Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

# Balanced Paranthesis Problem
# Stack Approach

class ParenthesisCheck:
    def isBalanced(self, s):
        stack = []
        mapping = {')': '(',
                   '}': '{',
                   ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

sample = ParenthesisCheck()
print(sample.isBalanced('()'))
# True

print(sample.isBalanced('()[]{}'))
# True

print(sample.isBalanced('([)]'))
# False

                