#Get user input for age as a string
age_str = input("Enter  your age")

#convert age_str to an integer
age= int(age_str)

#check the age condition and display the appropriate message
if age > 22:
    print("I dont care")
elif age == 18:
    print("You pass")
elif age < 17:
    print ("you cannot touch beer")
else:
    print("you can drink")