#CALCULATOR

def calculate(num1,num2,operation):
    if operation == '+':
        return num1+num2
    elif operation =='-':
        return num1-num2
    elif operation =='*':
        return num1*num2
    elif operation =='/':
        if num2!=0:
            return num1/num2
        else:
            return "Error:Division by Zero is not allowed."
    else:
        return"Invalid operation."
num1=float(input("Enter the first number:"))
num2=float(input("Enter the Second number:"))
operation=input("Enter an Operation (+,-,*,/):")
result=calculate(num1,num2,operation)
print("The result is:",result)