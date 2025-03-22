def is_even_or_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    try:
        number = int(input("Please enter a number: "))
        result = is_even_or_odd(number)
        print(result)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()