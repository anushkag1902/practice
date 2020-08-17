#creating console based calculator     using if-elif-else statement

num1=eval(input("enter your number:-"))
num2=eval(input("enter ur number:-"))

operation =input('''enter your operation which u want to perform
                      + for addition
                       - for substraction
                        * for multiplication
                         / for division
                         ''')

if(operation == '+'):
    output=num1+num2
    print(output)
elif(operation == '-'):
    output=num1-num2
    print(output)
elif(operation == '*'):
    output=num1*num2
    print(output)
elif(operation == '/'):
    output=num1/num2
    print(output)
else :
    print("enter a valid operation")                             