
# no  7. Write a program that asks the user for a password repeatedly until the correct password is entered.
correct_password = "admin123"

password = input("Enter password: ")

while password != correct_password:
    print("Wrong password. Try again.")
    password = input("Enter password: ")

print("Access Granted!")

# no 8 Write a program that keeps asking the user for numbers and stops when the user enters 0.
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter a number (0 to stop): "))

print("Program Ended") 

# n0 9. Write a program that counts how many digits are in a given number.
number = int(input("Enter a number: "))

count = 0

while number != 0:
    count += 1
    number //= 10

print("Number of digits:", count)