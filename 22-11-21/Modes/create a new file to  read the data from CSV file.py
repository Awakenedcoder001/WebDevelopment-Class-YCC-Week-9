import csv 
def csv_write(): 
 file_csv=open("csvwriting2.csv","w",newline="") 
 file_writer=csv.writer(file_csv) 
 file_writer.writerow(["NAME","ID","AGE","GENDER","COURSE"]) 
 n=int(input("ENTER THE NUMBER OF STUDENTS :")) 
 
 for i in range(n): 
  name=input("ENTER THE NAME:") 
  sid=input("ENTER THE ID :") 
  age=input("ENTER THE AGE :") 
  gender=input("ENTER THE GENDER :") 
  course=input("ENTER THE COURSE :") 
  file_writer.writerow([name,sid,age,gender,course]) 
  print(f"Person {i+1} details Successfully Stored") 
 
 file_csv.close() 
 
def csv_read(): 
 file_read=open("csvwriting1.csv") 
 file_reading=csv.reader(file_read) 
 print(file_read) 
 for i in file_reading: 
  #print(i) 
  for j in i: 
   print(j,end=' ') 
  print() 
 
 
if __name__== '__main__': 
 csv_write() 
 csv_read()