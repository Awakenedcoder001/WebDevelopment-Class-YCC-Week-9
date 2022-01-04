def execlusive():
    execlusive_mode=open("doophu.txt", 'x')
    execlusive_mode.write("This is the list for Tandin Dynasity\n")
    execlusive_mode.writelines(["Tandin\n", "Wangchu\n","Phurba\n", "from", "Bhutan\n","Thimpnu\n" ])
    execlusive_mode.close

if __name__ == "__main__":
    execlusive()