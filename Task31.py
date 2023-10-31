#Get user input for age as a string
age_str= input("Enter your age")

#convert age_str to an integer
age = int(age_str)

#check  if age is above 18 and display the appropriate massage
if age > 18:
    print("you can drink")
else:
    print("Please  grow older")