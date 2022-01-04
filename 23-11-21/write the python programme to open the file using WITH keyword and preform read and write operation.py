with open("writting.txt", "w")as file_write:
    file_write.writelines(["WWE wrestlers \n", "Hulkhogan\n", "Rock\n", "Rikishi\n", "John Cena\n", "Kane\n", "Undertaker\n", "Edge\n", "brocklesner\n"])
    print(f"File Name is : {file_write.name}")
    print(f"File Mode is : {file_write.mode}")
    print(f"File is closed:{file_write.closed}")
    print(f"File is closed:{file_write.closed}")

    with open("writing6.txt") as file_read:
        contents=file_read.read()
        print(f"FILE NAME IS : {file_read.name}")
        print(f"FILE MODE IS : {file_read.mode}")
        print(f"FILE IS CLOSED : {file_read.closed}") 
        print(f"CONTENTS OF THE FILE IS : \n {contents}") 
        print(f"FILE IS CLOSED : {file_read.closed}")
