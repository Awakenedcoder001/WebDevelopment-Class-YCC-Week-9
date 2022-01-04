def file_operation(): 
 try: 
  file_open=open("writing10.txt") 
  contents=file_open.read() 
  print(contents) 
 
 except FileNotFoundError as msg: 
  print(f"Cause Of The Exception is : {msg}") 
  print(f"Inside file_opertation function except method") 
  raise msg 
   
 except Exception as msg: 
  print(f"Cause Of The Exception is : {msg}") 
  raise msg 
 
def calling_function(): 
 try: 
  file_operation() 
 
 except Exception as msg: 
  print(f"Cause Of The Exception is : {msg}") 
  print(f"Inside calling function except method") 
  raise msg 
 
if name == '__main__': 
 try: 
  calling_function() 
 
 except Exception as msg: 
  print(f"Cause Of The Exception is : {msg}") 
  print(f"Inside if block Exception")


# Cause Of The Exception is : [Errno 2] No such file or directory: 'writing10.txt' 
# Inside file_opertation function except method 
# Cause Of The Exception is : [Errno 2] No such file or directory: 'writing10.txt' 
# Inside calling function except method 
# Cause Of The Exception is : [Errno 2] No such file or directory: 'writing10.txt' 
# Inside if block Exception 
 