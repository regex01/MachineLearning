import array

def greet(name):
    print(f"Hello, {name}!")

greet("GitHub Copilot")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(f"The factorial of 5 is: {result}")


# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Access elements of the array
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3

# Modify elements of the array
my_array[1] = 10
print(my_array)  # Output: array('i', [1, 10, 3, 4, 5])






