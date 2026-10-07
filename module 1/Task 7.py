a = int(input("amount: "))
b = str(input("(USD, EUR, PLN, TRY) Currency: "))
if (b == "USD"):
    print(int(a*44.86))
elif (b == "EUR"):
    print (int(a*50.21))
elif (b == "PLN"):
    print(int(a * 11.48))
elif (b == "TRY"):
    print(int(a * 0.91))