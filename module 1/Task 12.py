while True:
    a = float(input("num a:"))
    b = float(input("num b:"))
    symb = input("+, -, *, = (for average)")
    if symb == "+":
        print(f"{a} + {b} = {a+b}")
    elif symb == "-":
        print(f"{a} - {b} = {a-b}")
    elif symb == "*":
        print(f"{a} * {b} = {a*b}")
    elif symb == "=":
        print(f"average of {a} and {b} is {(a+b)/2}")
    else:
        print("I need COS bro😭🥀")