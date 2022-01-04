def properties1():
    properties1=open("writting1.txt", "w")
    print(f"The file name is: {properties1.name}")
    print(f"The file mode is: {properties1.mode}")
    print(f"The file is Closed: {properties1.closed}")
    print(f"The file is readable: {properties1.isreadable()}")
    print(f"The file is writeable: {properties1.iswriteable()}")
    properties1.close()
    print(f"The file mode is: {properties1.closed}")

if __name__ == "__main__":
    properties1()