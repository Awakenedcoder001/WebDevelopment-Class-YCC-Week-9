try:  
 acc_no=int(input("ENTER THE ACCOUNT NUMBER : ")) 
 password=int(input("ENTER THE ACCOUNT NUMBER: ")) 
 
 if acc_no == 200390490 and password == 123456789: 
  amount=int(input("ENTER THE AMOUNT TO WITHDRAW :")) #20000 
  totalbalace=10000 
  balance=totalbalace-amount  #10000 - 20000 = -10000 
  if balance<0:  #balance=10000 
   balance=totalbalace 
   totalbalace=balance 
   amount=10/0 #ZeroDIvisionError 
 
  else: 
   totalbalace=balance 
 
 else: 
  lst={1:1,2:2} 
  lst[3] 
 
except ZeroDivisionError as msg: 
 print("Insufficient Balance !!!") 
 
except KeyError as msg: 
 print("Invalid Account Number and Password") 
 
except Exception as msg: 
 print(f"SERVER DOWN !! TRANSACTION FAILED") 
 
else: 
 print("TRANSACTION SUCCESSFULL") 
 print(f"YOUR ACCOUNT BALANCE IS : {totalbalace}") 
 
finally: 
 print("ThankYou For Using Our Service!!!")
 #Results

# ENTER THE ACCOUNT NUMBER : 200390490
# ENTER THE ACCOUNT NUMBER: 123456789
# ENTER THE AMOUNT TO WITHDRAW :5000
# TRANSACTION SUCCESSFULL
# YOUR ACCOUNT BALANCE IS : 5000
# ThankYou For Using Our Service!!!

# ENTER THE ACCOUNT NUMBER : 200390490
# ENTER THE ACCOUNT NUMBER: 123
# Invalid Account Number and Password
# ThankYou For Using Our Service!!!
 
 
# ENTER THE ACCOUNT NUMBER : 200390490
# ENTER THE ACCOUNT NUMBER: 123456789  
# ENTER THE AMOUNT TO WITHDRAW :20000
# Insufficient Balance !!!
# ThankYou For Using Our Service!!!
 
 
# ENTER THE ACCOUNT NUMBER5100061010001 
# ENTER THE ACCOUNT NUMBER123456789 
# ENTER THE AMOUNT TO WITHDRAW :1000 
# TRANSACTION SUCCESSFULL 
# YOUR ACCOUNT BALANCE IS : 9000 
# ThankYou For Using Our Service!!! 

# ENTER THE ACCOUNT NUMBER5100061010001 
# ENTER THE ACCOUNT NUMBER1000 
# Invalid Account Number and Password 
# ThankYou For Using Our Service!!! 
 
