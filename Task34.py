temperature_str = input("Enter thr temperature")
temperature = int(temperature_str)

if temperature >=100:
    print("Boiling")
elif 32 <= temperature <= 99:
    print("Liquid")
else:
    print("Freezing")