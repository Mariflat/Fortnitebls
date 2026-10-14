import random

time = int(input("seconds from start of the day"))
ch = input("units (h, m, s):  ")
tLeft = 86400-time
randomN = random.randrange(2)
#print(round(643623.666))
if randomN == 0:
    if time == 86400:
        print("thy end is now")
        quit()
    elif time > 86400:
        print("You are late bro")
        quit()
    if ch == "h":
        print(f"{round((tLeft/60)/60)} hours left")
    elif ch == "m":
        print(f"{round((tLeft/60))} minutes left")
    elif ch == "s":
        print(f"{tLeft} second left")


    else:
        print("thy end is now")
else:
    print("Idk man")
