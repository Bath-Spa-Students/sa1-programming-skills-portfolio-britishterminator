#Exercise 10

def check_even_odd(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    # Ask the user for a number
    user_input = int(input("Enter a number: "))  # Convert input to integer
    # Call the function and print the result
    result = check_even_odd(user_input)
    print(result)

if __name__ == "__main__":
    main()


    