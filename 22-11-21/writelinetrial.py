def writelines():
    write_lines=open("writelines.txt","a")\n
    multiline=["Tandin","Tshewang", "Male" "Dota2"]
    write_lines.writelines(multiline)
    write_lines.close()


if __name__ == "__main__":
    writelines()