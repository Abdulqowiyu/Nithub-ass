import math

print("Triangle Area Calculator")
print("1. Base and Height")
print("2. Heron's Formula")

choice = int(input("Choose method (1 or 2): "))

if choice == 1:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    area = 0.5 * base * height
    print("Area =", area)

elif choice == 2:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("Area =", area)

else:
    print("Invalid choice")