if __name__== '__main__': 
 try: 
  #print("Opening a file that does not exist") 
  #file_read=open("writing7.txt") 
  file_read=open("writing6.txt") 
  print("File is in reading mode") 
  file_read=open("writing9.txt","x") 
  result=10/0 
  print(result) 
  d={1:1,2:2,3:3} 
  print(d[4]) 
  #print(d[3]) 
  #s={{1,2,3},{4,5,6}} 
  s=[1,2,3,4,5] 
  print(s) 
 
 except(FileNotFoundError,FileExistsError,ZeroDivisionError,Exception) as msg: 
  print(f"Cause of the exception is:{msg}") 
 
 finally: 
  print("Inside finally block")


  #RESULTS:D:\Python\fileoperations>python "try and except.py" 
#File is in reading mode 
#Cause of the exception is:[Errno 17] File exists: 'writing9.txt' 
#Inside finally block 
 
