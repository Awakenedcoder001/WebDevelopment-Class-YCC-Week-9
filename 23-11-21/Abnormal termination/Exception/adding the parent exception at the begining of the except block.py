if __name__== '__main__': 
 try: 
  #print("Opening a file that does not exist") 
  #file_read=open("writing7.txt") 
  file_read=open("writing6.txt") 
  print("File is in reading mode") 
  file_read=open("writing9.txt","x") 
  d={1:1,2:2,3:3} 
  #print(d[4]) 
  print(d[3]) 
  #s={{1,2,3},{4,5,6}} 
  s=[1,2,3,4,5] 
  print(s) 
  
 except Exception as msg: 
  print(f"cause of error is :{msg}") 
  print(f"Error Occurred") 
 
 except FileNotFoundError as msg: 
  print(f"cause of error is :{msg}") 
  print(f"File does not exists") 
 
 except FileExistsError as msg: 
  print(f"cause of error is :{msg}") 
  print(f"File is present") 
 
 except KeyError as msg: 
  print(f"cause of error is :{msg}") 
  print(f"key does not exists") 
 
 except TypeError as msg: 
  print(f"cause of error is :{msg}") 
  print(f"cause of the exception")

  #outputsOpening a file that does not exist 
# cause of error is :[Errno 2] No such file or directory: 'writing7.txt' 
# Error Occurred 
 

# File is in reading mode 
# cause of error is :[Errno 17] File exists: 'writing6.txt' 
# Error Occurred 
 

# File is in reading mode 
# cause of error is :4 
# Error Occurred 
 

# File is in reading mode 
# cause of error is :[Errno 17] File exists: 'writing7.txt' 
# Error Occurred 
 

# File is in reading mode 
# 3 
# cause of error is :unhashable type: 'set' 
# Error Occurred 
 

# File is in reading mode 
# cause of error is :[Errno 17] File exists: 'writing8.txt' 
# Error Occurred 
 

# File is in reading mode 
# 3 
# [1, 2, 3, 4, 5] 