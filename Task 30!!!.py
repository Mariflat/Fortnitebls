a = int(input("Start number:" ))
b = int(input("End number: "))
q = int(input("List order(1, 2):"))
if q==1:
    if b>a:
        for i in range(a, b+1, 1):
            print(i)
    if a>b:
        print("number order is reverted")
        for i in range(b, a+1, 1):
            print(i)
elif q == 2:
    if b > a:
        for i in range(b, a - 1, -1):

            print(i)
    if a > b:
        print("number order is reverted")
        for i in range(a, b - 1, -1):

            print(i)
else:
    print("...")