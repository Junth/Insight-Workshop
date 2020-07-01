# Question 17: Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

def calculator(a, b, op):
    try:
        return eval(str(a)+str(op)+str(b))
    except ZeroDivisionError:
        return f"Division by Zero"
        
    
print(calculator(5, 3, '+'))
# 8

print(calculator(5, 3, '-'))  
# 2

print(calculator(5, 3, '*'))
# 15

print(calculator(5, 10, '/'))
# 0.5

print(calculator(5, 0, '/'))
# Division by Zero