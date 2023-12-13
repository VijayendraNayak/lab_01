def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Get the number of rows for the triangle from the user
num_rows = int(input("Enter the number of rows for the triangle: "))

# Call the function to print the triangle
print_triangle(num_rows)
