#Ask the user to input a maximum age. 
#Then fetch user data from the API and print a summary of users who are younger
#than that age. Print their full name, email, age, and a message like 
#"This user is young" or "This user is middle-aged" depending on age

#Name: Jack Smith
#Age: 25
#Email: jack@example.com
#This user is young.

#https://dummyjson.com/users


import requests
x = requests.get('https://dummyjson.com/users')
data = x.json()

age = int(input("Please Enter the Age:"))

for user in data['users']:
    if user['age'] < age:
        print(f"Name: {user['firstName']} {user['lastName']}")
        print(f"Age: {user['age']}")
        print(f"Email: {user['email']}")

        if user['age'] < 30:
            print("This user is Young")

        else:
            print("This user is Middle-aged")
        
        print("-" * 30)