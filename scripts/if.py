running = True
while running:
    time = int(input("Enter a time:"))
    if time >= 1 and time <= 8:
        print("quick midnight snack")
    elif time >= 9 and time <= 12:
        print("breakfast")
    elif time >= 13 and time <= 18:
        print("lunch")
    elif time >= 19 and time <= 24:
        print("dinner")
    else:
        print("thats not a valid time, please try again")
        continue

