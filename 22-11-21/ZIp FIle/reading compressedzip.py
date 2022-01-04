from zipfile import * 
 
zipread=ZipFile("DOCUMENTS.zip","r",ZIP_STORED) 
name_list=zipread.namelist() 
print(name_list) 
 
for filename in name_list: 
 file_read=open(filename) 
 print(f"FILE NAME IS : {file_read.name}") 
 print(f"FILE MODE IS : {file_read.mode}") 
 contents=file_read.read() 
 print(contents) 
 print("=="*20)