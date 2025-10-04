#Simple Program to calcucate amout of banknotes(In this case Thai Baht)between range 2000 - 10000

while True: #create an infinite loop
    Balance = input("Balance(2000-10,000) : ")
    if Balance.isdigit(): #check if variable is a digits or not 
       num = int(Balance)
       if 2000 <= num <= 10000:
          print(num//1000)
          print(num//500)
          print(num//100)
           break #break the loop
       else:
            print("Balance out of range. Try agian")
    else:
        print("please enter a valid number")

input("Press Enter to exit...")

