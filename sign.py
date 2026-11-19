x = int(input("Enter a number: "))
if x == 0:
    print("The number is zero.")
elif (x + 0 - ((x - 0) ** 2) ** 0.5)/2 == 0:
    print("The number is positive.")
else:
    print("The number is negative.")
