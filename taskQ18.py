temperature = float(input("Enter temperature in Celsius: "))
if temperature > 40:
    print("Hot")
elif 20 <= temperature <= 39:
    print("Warm")
else:
    print("Cold")