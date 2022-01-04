def perform_operation(): 
 num1=int(input("Enter the numerator : ")) 
 #10 
 num2=int(input("Enter the denominator : ")) 
 #0 
 result=num1/num2 #error  
 print(result) 
if __name__== '__main__': 
 print("Inside the If Block") 
 perform_operation() 
 print("Control is back to If Block")

#  D:\Python\fileoperations>python exceptions.py 
# Inside the If Block 
# Enter the numerator : 10 
# Enter the denominator : 0 
# Traceback (most recent call last): 
#   File "D:\Python\fileoperations\exceptions.py", line 12, in <module> 
#     perform_operation() 
#   File "D:\Python\fileoperations\exceptions.py", line 6, in perform_operation 
#     result=num1/num2 #error 
# ZeroDivisionError: division by zero 
