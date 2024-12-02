from calc import add,sub,mult,div

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
command = input("Enter command (mult,div,add or sub): ")

while(command!= "stop"):
    if(command == "add"):
        print(add(num1,num2))
    elif(command == "sub"):
        print(sub(num1,num2))    
    elif(command == "mult"):
        print(mult(num1,num2))
    elif(command == "div"):
        if(num2 == 0):
            print("Can't divide by zero")
        else:
            print(div(num1,num2))
    else:
        print("invalid operation")
       
    print("If you want to do more operations type \yes\ ")
    print("If you don't want to do more operations type \stop\ ")
    command = input("Enter command (yes or stop): ")
    
    if(command == "yes"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        command = input("Enter command (mult,div,add or sub): ")
    elif(command == "stop"):
        break
    else:
        print("invalid input,Try again")
        command = input("Enter command (yes or stop): ")
   
               