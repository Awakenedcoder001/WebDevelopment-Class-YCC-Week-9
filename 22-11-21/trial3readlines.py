def read_lines():
    read_file=open("doophu.txt",'r')
    read_contents=read_file.readlines()
    print(read_contents)
    print(type(read_contents))

    for contents in read_contents:
        print(contents)
if __name__ == '__main__':
    read_lines()
    