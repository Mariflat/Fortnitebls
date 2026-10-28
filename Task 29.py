a = int(input("Start number:" ))
b = int(input("End number: "))
if b>a:
    for i in range(b, a-1, -1):
        if i%2 == 0:
            print(i)
if a>b:
    print("number order is reverted")
    for i in range(a, b-1, -1):
        if i%2 == 0:
            print(i)