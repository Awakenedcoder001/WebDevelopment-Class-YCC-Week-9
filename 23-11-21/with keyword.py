with open("writing6.txt","w") as file_write: 
 file_write.writelines(["WWE wrestlers\n","Hulk\n","Rikishi\n","Rock\n","Omega\n","Goldsberg\n"]) 
 print(f"FILE NAME IS : {file_write.name}") 
 print(f"FILE MODE IS : {file_write.mode}") 
 print(f"FILE IS CLOSED : {file_write.closed}") 
 
print(f"FILE IS CLOSED : {file_write.closed}") 
 
with open("writing6.txt") as file_read: 
 contents=file_read.read() 
 print(f"FILE NAME IS : {file_read.name}") 
 print(f"FILE MODE IS : {file_read.mode}") 
 print(f"FILE IS CLOSED : {file_read.closed}") 
 print(f"CONTENTS OF THE FILE IS : \n {contents}") 
 
print(f"FILE IS CLOSED : {file_read.closed}")