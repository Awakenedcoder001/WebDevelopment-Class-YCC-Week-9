from zipfile import * 
def zipping(): 
 documents=ZipFile("DOCUMENTS.zip","w",ZIP_DEFLATED) 
 documents.write("writing3.txt") 
 documents.write("writing1.txt") 
 documents.write("writing2.txt") 
 
if __name__== '__main__': 
 zipping()