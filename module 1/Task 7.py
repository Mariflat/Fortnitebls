a = int(input("amount: "))
b = str(input("(USD, EUR) Currency: "))
if (b == "USD"):
    print(int(a*44.86), "USD")
elif (b == "EUR"):
    print (int(a*50.21), "EUR")