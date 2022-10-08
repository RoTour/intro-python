a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

a, b, c = int(a), int(b), int(c)

if a < b and a < c:
    print(f"a ({a}) is the smallest number")
elif b < a and b < c:
    print(f"b ({b}) is the smallest number")
else:
    print(f"c ({c}) is the smallest number")

if a > b and a > c:
    print(f"a ({a}) is the largest number")
elif b > a and b > c:
    print(f"b ({b}) is the largest number")
else:
    print(f"c ({c}) is the largest number")
