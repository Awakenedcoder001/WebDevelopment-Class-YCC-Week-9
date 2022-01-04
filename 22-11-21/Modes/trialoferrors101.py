import csv 
def csv_operation(): 
    write_file=open("writing.csv","w") 
    csv_writer=csv.writer(write_file) 
    csv_writer.writerow(["Favouite Actors","Prabhas","Punnerth Rajkumar","Allu Arjun","jr.NTR","Ram Charan"]) 
    print("DATA IS STORED SUCCESSFULLY") 
 
if __name__== '__main__': 
    csv_operation()