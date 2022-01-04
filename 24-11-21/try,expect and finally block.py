def file_operation(): 
 try:  
  file_read=open("writing2.txt") 
  contents=file_read.read() 
  print(contents) 
  result=10/20 
  #result=10/0 
  print(result) 
  #file_read.close() 
 
 except FileNotFoundError as msg: 
  print("INSIDE EXCEPT BLOCK OF FILENOTFOUND") 
  print(f"CAUSE OF THE EXCEPTION IS : {msg}") 
  raise msg 
 
 except Exception as msg: 
  print("INSIDE PARENT EXCEPTION BLOCK") 
  print(f"CAUSE OF THE EXCEPTION IS : {msg}") 
  raise msg 
 
 finally: 
  print("INSIDE FINALLY BLOCK") 
  file_read.close() 
  print(f"IS FILE COLSED : {file_read.closed}") 
 
if name == '__main__': 
 try: 
  file_operation() 
 except Exception as msg: 
  print("INSIDE IF BLOCK OF PARENT EXCEPTION") 
  print(f"CAUSE OF THE EXCEPTION IS : {msg}")