num1 = float(input("first number:"))
num2 = float(input("second number:"))
num3 = float(input("third number:"))
symb = input("enter symbol (+, *):")

if symb == "+":
    print(f"sum of three numbers is: {num1 + num2 + num3}")
elif symb == "*":
    print(f"multiplication of three numbers is: {num1 * num2 * num3}")
else:
    print("sum shi bro")