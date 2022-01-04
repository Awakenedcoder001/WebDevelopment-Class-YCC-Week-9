#Opening the file for read and write 
 file_read=open("writing3.txt") 
 file_write=open("writing6.txt","x") 
 
 #Reading the contents from the file 
 reading_contents=file_read.read() 
 print(reading_contents) 
 
 #Writing the contents of the file to new file 
 file_write.write(reading_contents) 
 print("Completed the operation successfully") 
 
if name == '__main__': 
 read_write()