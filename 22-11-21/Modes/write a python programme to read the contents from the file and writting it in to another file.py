def read_write():
    #Opening the file for read and write:
    file_read=open('writting3.txt','r')
    file_read=open('writting.txt','x')

    #reading the contents
    reading_contents=file_read.read()
    print(reading_contents)

    #writting the contents of the file to a new file
file_write.write=open('writting.txt')



if __name__ == '__main__':
    read_write()