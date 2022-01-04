if __name__== '__main__': 
  try: 
   num1=int(input("Enter the numerator : ")) 
   num2=int(input("Enter the denominator : ")) 
   file_read=open("writing6.txt") 
   print("File is in reading mode") 
   lst_1=[1,2,3,4,5] 
   #print(lst_1[10]) 
   print(lst_1[1]) 
   print("Performing Division Operation") 
   result=num1/num2 
   print(f"Result is  : {result}") 
   d={1:1,2:2,3:3} 
   #print(d[4]) 
   print(d[3]) 
   
  except FileNotFoundError as msg: 
   print(f"cause of error is :{msg}") 
   print(f"File does not exists") 
 
  except IndexError as msg: 
   print(f"cause of error is :{msg}") 
   print(f"Index is not present") 
 
  except ZeroDivisionError as msg: 
   print(f"cause of error is :{msg}") 
   print(f"can not divide by zero") 
 
  except Exception as msg: 
   print(f"cause of error is :{msg}") 
   print(f"Error Occurred")


   #Output
# Enter the numerator : 10 
# Enter the denominator : 20 
# cause of error is :[Errno 2] No such file or directory: 'writing7.txt' 
# File does not exists 
 

# Enter the numerator : 10 
# Enter the denominator : 20 
# File is in reading mode 
# cause of error is :list index out of range 
# Index is not present 
 
# Enter the numerator : 20 
# Enter the denominator : 0 
# File is in reading mode 
# 2 
# Performing Division Operation 
# cause of error is :division by zero 
# can not divide by zero 
 
# Enter the numerator : 10 
# Enter the denominator : 2 
# File is in reading mode 
# 2 
# Performing Division Operation 
# Result is  : 5.0 
# cause of error is :4 
# Error Occurred 
 
# Enter the numerator : 10 
# Enter the denominator : 2 
# File is in reading mode 
# 2 
# Performing Division Operation 
# Result is  : 5.0 
# 3 
 