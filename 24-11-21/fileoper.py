def file_destruction():
    try:
        reader=open("newfile.txt", 'r')
        storage=reader.read()
        print(storage)
    except FileNotFoundError as letter:
        print("Inside of the except BLOCK OF FIEL NOT FOUND")
        print(f"The error which has led to the error is : {letter}")
        raise letter

    except Exception as letter:
        print("Inside of parent exception except block")
        print(f"The cause of the erroe which has led to the down fall is {letter}")
        raise letter


if __name__ == "__main__":
    try:
        file_destruction()
    except Exception as letter:
            print(f"Lets end thos shall we")
            print(f"Inside of the parent last parent block{letter}")
            





