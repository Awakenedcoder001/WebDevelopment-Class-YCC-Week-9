def append_mode(): 
 file_append=open("writing1.txt",'a') 
 file_append.write("This is a new line\n") 
 file_append.write("Hello World!!") 
 file_append.write("Completed Writing") 
 
 file_append.write("a=10") 
 
 
def append_mode_file(): 
 file_append=open("writing2.txt",'a') 
 file_append.write("This is a new line\n") 
 file_append.write("Hello World!!\n") 
 file_append.write("Completed Writing\n") 
 
 file_append.write("a=10") 
 
 
if __name__ == '__main__': 
 append_mode() 
 append_mode_file()