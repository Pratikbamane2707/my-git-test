import sys
print("Enter the choice in between 1 to 4 \n 1-add \n 2-Sub \n 3-multiply \n 4-divide ")
operation = int(sys.argv[1])
num1=float(sys.argv[1])
num2=float(sys.argv[2])

if operation==1:
    print(f'The addition of {num1} and {num2} is {num1+num2}')

elif operation==2:
    print(f'The Substraction of {num1} and {num2} is {num1-num2}')
elif operation==3:
    print(f'The Multiplication of {num1} and {num2} is {num1*num2}')
elif operation==4:
    print(f'The Division of {num1} and {num2} is {num1/num2}')
else:
    print('Enter in between 1 to 4 you are entering wrong')
