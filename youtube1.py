#create a console based calculator         using if statement
num1 =eval(input("enter your first number :-"))
num2 =eval(input("enter your first number :-"))
operation =input('''enter your operation which u want to perform
                      + for addition
                       - for substraction
                        * for multiplication
                         / for division
                         ''')
if (operation =='+'):
    output = num1+num2
    print(output)

if (operation =='-'):
    output = num1-num2
    print(output)

if (operation =='*'):
    output = num1*num2
    print(output)

if (operation =='/'):
    output = num1/num2
    print(output)