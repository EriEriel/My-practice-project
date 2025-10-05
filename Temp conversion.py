while True:
    
 print( "====Option====")
 print("Celsius To Fahrenheit Press 1")
 print("Fahrenheit To Celsius Press 2")

 x = (input("Select option 1 or 2 \n: "))
 if x in ["1","2"]:
        Option = float(x)
        if Option == 1:
            c = float(input("Celsius : "))
            f = c*9/5+32
            print(f"{c} Celsius = {f} Fahrenheit")
            break
        if Option == 2:
            f = float(input("Fahrenheit : "))
            c = (f-32)*5/9
            print(f"{f} Fahrenheit = {c} Celsius")
            break
   
 else:
        print("Invalid Input")



#  print(f"{c} Celsius = {f} Fahrenheit") the first f is f-string with is formatted string allow to insert variable or expression directly into string     

        
            
        
    
