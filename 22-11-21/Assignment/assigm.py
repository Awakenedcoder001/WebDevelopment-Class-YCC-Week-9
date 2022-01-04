def read_operation():
    anmt=open("assignment.rtf")
    file_contents=anmt.read()
    print(file_contents)
    anmt.close
if __name__ == "__main__":
    read_operation()