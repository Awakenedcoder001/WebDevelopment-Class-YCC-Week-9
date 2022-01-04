def read_operation(): 
 read_file=open("writing3.txt","r") 
 print("File is openened for reading") 
 file_contents=read_file.read(10) 
 print(file_contents) 
 read_file.close() 
 
if name == '__main__': 
 read_operation()