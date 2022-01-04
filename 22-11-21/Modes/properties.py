def properties(): 
    properties=open("writing5.txt","w+") 
    print(f"The file name is : {properties.name}") 
    print(f"The file mode is : {properties.mode}") 
    print(f"The file is Closed: {properties.closed}") 
    print(f"The file is Readable : {properties.readable()}") 
    print(f"The file is Writable : {properties.writable()}") 
    properties.close() 
    print(f"The file is closed : {properties.closed}") 
 
if __name__ == '__main__': 
    properties()