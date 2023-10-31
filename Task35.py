day = input("Enter the day :")
if day in {"Monday","Tuesday","wednasday","thursday"}:
    print("weekday")
elif day=="friday":
    print("TGIF")
elif day in {"saturday","sunday"}:
    print("weekend")
else:
    print("invail input")