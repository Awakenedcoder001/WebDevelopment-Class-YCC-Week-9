def exclusive(): 
 exclusive_mode=open("writing3.txt","x") 
 exclusive_mode.write("These are Legends Of Bowing\n") 
 exclusive_mode.writelines(["Breet lee\n","Mcgrath\n","Shane Bond\n","Gillispe\n","Warne\n","Kumble\n"]) 
 exclusive_mode.close() 
 
if __name__== '__main__': 
 exclusive()