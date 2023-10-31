# Get user inputs for grade as a string
grade_str = inputs("Enter your grade")

#convert grade_str to an integer
grade = int(grade_str)

#check thre grade conditions and display the appropriate message
if garde >=90:
    print("A")
elif 80<= grade <=89:
    print("8")
elif 70<=grade <= 79:
    print("C")
else:
    print("F")