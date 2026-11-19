a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
d = int(input("Enter a fourth number: "))
temp = 0

if a > b:
    temp = a
    a = b
    b = temp

if b > d:
    temp = b
    b = d
    d = temp

if a > c:
    temp = a
    a = c
    c = temp

if b > c:
    temp = b
    b = c
    c = temp

if c > d:
    temp = c
    c = d
    d = temp

print("The numbers in ascending order are:", a, b, c, d)
