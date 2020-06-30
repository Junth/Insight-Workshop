# Question 10: Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


def camel_snake(CamelCase, separator):
    return ''.join([separator + char.lower() if char.isupper() else char
                    for char in CamelCase]).lstrip(separator)
   

CamelCase = 'ThisIsCamelCased'

# CamelCase to snake_case
print(camel_snake(CamelCase, '_'))
# this_is_camel_cased


# CamelCase to kebab-case
print(camel_snake(CamelCase, '-'))
# this-is-camel-cased