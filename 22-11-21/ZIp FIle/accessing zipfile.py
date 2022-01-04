from zipfile import *
zipread=ZipFile('Documents.zip','r', ZIP_STORED)
name_list=zipread.namelist()
print(name_list)

for filename in name_list:
    print(f"File name would be {file_read.name}:")
    print(f"File mode would be {file_read.mode}:")
    contents = file_read.read()
    print(contents)
    print('=='*20)

    