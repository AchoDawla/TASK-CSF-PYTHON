#Define  a variable called "score" and get its from user input
score = input("Enter your score:")
#convert the input to an integer 
score= int(score)
#check the score 
if score >=90:
    print("A")
elif score >=80 and score <=89:
    print("B")
elif score >=70 and score <=79:
    print("c")
elif score >=60 and score <=69:
    print("D")
elif score < 60:
    print("F")
else:
    print("Invailed score")