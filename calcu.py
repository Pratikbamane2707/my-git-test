import sys
print("Enter the choice in between 1 to 4 \n 1-add \n 2-Sub \n 3-multiply \n 4-divide ")
choice = int(sys.argv[1])
num1=float(sys.argv[2])
num2=float(sys.argv[3])

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
