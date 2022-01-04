try:
    account_no=int(input("Ente the user name : "))
    password_no=int(input("Enter the password : "))
    if account_no == 200390490 and password_no == 12324252:
        amount=int(input("Enter the Amount to withdraw : "))
        totalbalance= 10000
        balance= totalbalance - amount #10000-20000    
        if balance < 0:   #-10000
            balance=totalbalance
            totalbalance= balance
            result = 10/0 #Error ZeroDivisionError
        
        else:
            totalbalance= balance
    else:
        lst={1:1,2:2}
        lst=[3]
except ZeroDivisionError as msg:
    print("Balance is insufficent")
# except KeyError as msg:
#     print("Wront account number or password")
except Exception as msg:
    print("The ATM is out of service, please try again later")
else:
    print("Transaction completed")
    print(f"Your remaining balance is : {balance}")

finally:
    print("Thank you for using our service")

