# Taking input from user
num = int(input("Enter a number: "))

# Initialize factorial
fact = 1

# Check for negative number
if num < 0:
    print("Factorial not defined for negative numbers")

else:
    # Calculate factorial using loop
    for i in range(1, num + 1):
        fact = fact * i

    # Display result
    print("Factorial of", num, "is:", fact)
