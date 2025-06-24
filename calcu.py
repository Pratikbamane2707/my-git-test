print("Enter the choice in between 1 to 4 \n 1-add \n 2-Sub \n 3-multiply \n 4-divide ")
choice = int(input('Your choice:'))
num1=float(input('Enter the first number -- '))
num2=float(input('Enter the second number -- '))

if choice==1:
    print(f'The addition of {num1} and {num2} is {num1+num2}')

elif choice==2:
    print(f'The Substraction of {num1} and {num2} is {num1-num2}')
elif choice==3:
    print(f'The Multiplication of {num1} and {num2} is {num1*num2}')
elif choice==4:
    print(f'The Division of {num1} and {num2} is {num1/num2}')
else:
    print('Enter in between 1 to 4')
