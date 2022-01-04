def image_operation():
    image_read=open("dophu.jpeg","rb")
    content=image_read.read() 
 #print(content) 

    image_write=open("copyofdophu.jpeg","wb")
    image_write.write(content)
    print(f"IMAGE IS COPIED SUCCESSFULLY") 

    image_read.close()
    image_write.close() 
 
 
def mp_operation():
    mp3_read=open("html.mp3","rb")
    content=mp3_read.read() 
 #print(content) 
 
    mp3_write=open("htmlcopy.mp3","wb")
    mp3_write.write(content)
    print(f"AUDIO IS COPIED SUCCESSFULLY") 
    mp3_read.close()
    mp3_write.close() 
 
def mp4_operation():
    mp4_read=open("html.mp4","rb")
    content=mp4_read.read() 
 #print(content) 
 
    mp4_write=open("htmlcopy.mp4","wb")
    mp4_write.write(content)
    print(f"VEDIO IS COPIED SUCCESSFULLY") 
 
    mp4_read.close()
    mp4_write.close() 
 
if __name__== '__main__':
    image_operation()
    mp_operation()
    mp4_operation()