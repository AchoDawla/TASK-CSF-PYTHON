num1 = int(input("Enter the first nummber: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    num1, num = num2, num1
total_sum = 0
while num1 <= num2:
    total_sum +=num2
    num1 += 1
print("The sum of numbers between" , "and", num2, "is", total_sum)