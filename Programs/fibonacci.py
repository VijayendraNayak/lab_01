def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

# Get the number of terms for the Fibonacci series from the user
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

# Call the function to generate the Fibonacci series
result = fibonacci(num_terms)

# Print the Fibonacci series
print("Fibonacci Series:")
print(result)
