# Voter Eligibility Checker

age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ").lower()
registered = input("Are you registered to vote? (yes/no): ").lower()

if age >= 18 and citizenship == "yes" and registered == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")