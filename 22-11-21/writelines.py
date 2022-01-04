def write_lines(): 
 write_lines=open("writelines.txt","w") 
 multiline=["Sachin\n","Dravid\n","Gavaskar\n","Michael Bevan\n","Lara\n","Ponting"] 
 write_lines.writelines(multiline) 
 write_lines.close() 
 
if __name__=="__main__": 
 write_lines()