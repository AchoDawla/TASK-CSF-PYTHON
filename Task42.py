#Get the name from the user
user_name = input("Enter your name:")
#convert the input to lowercase for case-insensitivity matching
user_name.lower()
#initialize a variable to False
has_vowel=False
#list of vowels
vowels= {'a','e','i','o','u'}
#Initailize an index to 0
index = 0
while index < len(user_name) and not has_vowel:
    if user_name[index]in vowels :
        has_vowel = True
    index +=1
print(has_vowel)
