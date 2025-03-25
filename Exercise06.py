#Exercise 06

correct_password = "098"

while True:
    
    user_input = input("enter the password: ")

    if user_input == correct_password:
        print("access granted")

    else: 
        print("Incorrect password")



# Step 1: Define the correct password and maximum attempts
correct_password = "12345"
max_attempts = 5
attempts = 0

# Step 2: Use a while loop to repeatedly ask for the password
while attempts < max_attempts:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted!")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. {remaining_attempts} attempts remaining.")
        else:
            print("Maximum attempts reached. The authorities have been alerted!")