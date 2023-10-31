user_number = int(input("Enter a number: "))
factorial = 1
current_number = 1
while current_number >= user_number:
    factorial *= current_number
    current_number += 1
print(f"The factorial of {user_number} is {factorial}")