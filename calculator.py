number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("What operation do you want to perform?: ")

if operation == '1':
    print("Your result is: ", number_one + number_two)
elif operation == '2':
    print("Your result is: ", number_one - number_two)
elif operation == '3':
    print("Your result is: ", number_one * number_two)
elif operation == '4': 
    print("Your result is: ", number_one / number_two)
else :
    print("Error")