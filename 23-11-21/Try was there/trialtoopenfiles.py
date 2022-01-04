def image_operation():
    balu=open("download.jfif", 'rb')
    store=balu.read()

    copybear=open("copycatbalu.jfif", 'wb')
    copybear.write(store)
    print(f"IMAGE IS COPIED SUCCESSFULLY")

    balu.close()
    copybear.close()

def mp_operation():
    muzik=open("Yumtsho.mp3", 'rb')
    holder=muzik.read()

    jutsu=open("CopyofYumtsho.mp3", 'wb')
    jutsu.write(holder)

    muzik.close()
    jutsu.close()

def mp4_operation():
    bideo=open("Katmandu.mp4", 'rb')
    chinatown=bideo.read()

    town=open("Chinabazar.mp4", 'wb')
    town.write(chinatown)
    print("china town ready")


if __name__ == '__main__':
    image_operation()
    mp_operation()
    mp4_operation()
