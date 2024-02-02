# PREP 
# Params:n
# Return: sum of prior two numbers
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# Pseudocode:
# - take first and second number and get the sum
# - make sum equal to third number
# - add second and third number for sum of 4th, and so on
# - return the sum of each number corresponding to whatever n is



def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

