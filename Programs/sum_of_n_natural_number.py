def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

# Get the value of n from the user
n = int(input("Enter the value of n: "))

# Call the function to calculate the sum of the first n natural numbers
result = sum_of_natural_numbers(n)

# Print the result
print(f"The sum of the first {n} natural numbers is: {result}")