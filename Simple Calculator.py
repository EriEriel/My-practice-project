while True:
    print("Welcome to the Goddamn simple Calculator programe")
    print("Please use format ( a operator b )")
    print("Please put space between each value")
    Equation = input("Insert your Equation here : ").split()

    a = float(Equation[0])
    b = (Equation[1])
    c = float(Equation[2])

    if b == "+":
        x = a + c
        print(x)

    elif b == "-":
        x = a - c
        print(x)

    elif b == "*":
        x = a * c
        print(x)

    elif b == "/":
        x = a / c
        print(x)

    else:
        print("invalid input")

    Loop = input("Do you want another calculation Y/N \n: ")
    if Loop.lower() == "n":
         print("Program End")

         break
   

 
        
            

   

   
        
    
        
