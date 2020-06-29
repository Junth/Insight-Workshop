# Question 2: Write an if statement to determine whether a variable holding a year
# is a leap year.

sample_year = 2008
result = sample_year % 4 == 0 or (sample_year % 100 == 0 and sample_year % 400 == 0)
print(result)