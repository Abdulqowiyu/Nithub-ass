print("Height Converter")

height = float(input("Enter height: "))
unit = input("Enter unit (m, cm, ft, in): ").lower()

if unit == "m":
    print("Centimeters:", height * 100)
    print("Feet:", height * 3.28084)
    print("Inches:", height * 39.3701)

elif unit == "cm":
    print("Meters:", height / 100)
    print("Feet:", height / 30.48)
    print("Inches:", height / 2.54)

elif unit == "ft":
    print("Meters:", height / 3.28084)
    print("Centimeters:", height * 30.48)
    print("Inches:", height * 12)

elif unit == "in":
    print("Meters:", height / 39.3701)
    print("Centimeters:", height * 2.54)
    print("Feet:", height / 12)

else:
    print("Invalid unit entered.")