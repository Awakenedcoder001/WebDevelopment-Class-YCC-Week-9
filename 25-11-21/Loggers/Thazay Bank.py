import logging 
logging.basicConfig(filename="thazaybank.txt",level=logging.DEBUG,format='%(asctime)s:: %(levelname)s :: %(message)s',datefmt="%d-%m-%y %H:%M:%S") 
 
try:   
    acc_no=int(input("ENTER THE ACCOUNT NUMBER"))  
    password=int(input("ENTER THE ACCOUNT NUMBER"))  
 
    if acc_no == 5100061010001 and password == 123456789:  
        amount=int(input("ENTER THE AMOUNT TO WITHDRAW :")) #20000  
        logging.info(f"AMOUNT ENTERED TO WITHDRAW : {amount}" ) 
        totalbalace=10000  
        logging.info(f"TOTAL AMOUNT IN THE ACCOUNT BEFORE WITHDRAWING: {totalbalace}" ) 
         
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
     msg="INSUFFICUENT FUNDS !!" 
     logging.exception(msg) 
  
except KeyError as msg:  
    msg="Invalid Account Number and Password"  
    logging.exception(msg)  ##### why do we use exception here
 
except Exception as msg:  
    msg="SERVER DOWN !! TRANSACTION FAILED"  
    logging.exception(msg) 
    logging.info(f"TOTAL AMOUNT IN THE ACCOUNT AFTER WITHDRAWING: {totalbalace}" ) 
         
 
else:  
    msg=("TRANSACTION SUCCESSFULL") 
    print(f"YOUR ACCOUNT BALANCE IS : {totalbalace}")  
    logging.info(f"YOUR ACCOUNT BALANCE IS : {totalbalace}")  
    logging.info(msg) 
 
finally:  
    print("ThankYou For Using Our Service!!!") 
    logging.info("CASH COLLECTED !!")