import logging 
logging.basicConfig(filename="25-11-2021.txt",level=logging.DEBUG,filemode="w") 
logging.critical("Critical Needs Action immediately") 
logging.error("Error Occured") 
logging.warning("warning") 
logging.info("Some one has logged in !!") 
logging.debug("Debugging Successfull!") 
#logging.notset("notset")