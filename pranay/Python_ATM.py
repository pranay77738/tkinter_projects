print('Welcome to the Python ATM')
restart=('Y')
chances=3
balance=999.12

while chances >= 0:
    pin=int(input("Enter your ATM pin :"))
    if pin == (1234):
        print("You entered your ATM pin correctly")
        print("Please press 1 for your Balance")
        print("Please press 2 for make a Withdrawal")
        print("Please press 3 for the Pay In")
        print("Please press 4 to withdraw your card \n")
        

        while restart not in ('n',"N","NO","no","No","nO"):
            print("You entered your ATM pin correctly")
            print("Please press 1 for your Balance")
            print("Please press 2 for make a Withdrawal")
            print("Please press 3 for the Pay In")
            print("Please press 4 to withdraw your card \n")

            option=int(input("What would you like to choose? :"))

            if option == 1:
                print("Your Balance is ",balance)
                restart=input("Would you like to go back ")

                if restart in ('n',"N","NO","no","No","nO"):
                    print("Thank you")
                    break
            elif option == 2:
                option2 = ("y") 
                withdraw=float(input("How much would you like to withdraw ? 10,20,30,40,50,100 for other enter 1 :2"))

                if withdraw in [10,20,30,40,50,100]:
                    print("Your Balance is {}".format(balance-withdraw))
                    restart=input("Would you like to go back ")

                    if restart in ('n',"N","NO","no","No","nO"):
                        print("Thank you")
                        break

                elif withdraw != [10,20,30,40,50,100]:
                    print("Invalid amount entered Re-try \n")
                    restart=('y')

                elif withdraw == 1:
                    withdraw=float(input("Please Enter a Desired amount :"))    

            elif option == 3:
                pay_in= float(input("How much would you like to pay-in :"))  
                print("your Balance is now {}".format(balance+pay_in))
                restart=input("Would you like to go back ")

                if restart in ('n',"N","NO","no","No","nO"):
                    print("Thank you")
                    break

            elif option == 4:
                print("Wait while your card is Returned \n")
                print("Thank you for your service")
                break

            else:
                print("Please enter a correct number ")
                restart=("y")
    elif pin != (1234):
        print("Please enter a correct pin")    
        chances -=1
        if chances == 0:
            print("You Entered wrong pin thrice try again")      
            break     


