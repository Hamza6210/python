#Ask the user to input a maximum age. 
#Then fetch user data from the API and print a summary of users who are younger
#than that age. Print their full name, email, age, and a message like 
#"This user is young" or "This user is middle-aged" depending on age

#Name: Jack Smith
#Age: 25
#Email: jack@example.com
#This user is young.

#https://dummyjson.com/users


print("Please enter the age: ")
age = input()

import requests
x = requests.get('https://dummyjson.com/users')
data = x.json()
print(data)