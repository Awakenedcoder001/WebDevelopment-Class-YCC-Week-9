def read_operation():
    read_file=open("doophu.txt")
    read_file_1=open("writting.txt")
    print("File has been opened for readibg")
    file_contents=read_file.read()
    file_contents_1=read_file_1.read()
    print(file_contents)
    read_file.close()
    read_file_1.close()



if __name__ == "__main__":
    read_operation()

