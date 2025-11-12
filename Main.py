#print("Hello World" , end=" ")
#print("Hi World")
#print("Hi my name is Hamza and I'm" , 35 , "years old")

#x = 45
#y = 35 
#if x < y :
#    print("y is greater than x")
#else:
#    print("x is greater than y")


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")   

check = '.' in num1 or '.' in num2

if check:
    result = float(num1) + float(num2)
    print(f"The Sum is: {float(result)}")

else:
    result = int(num1) + int(num2)
    print(f"The sum is: {int(result)}")