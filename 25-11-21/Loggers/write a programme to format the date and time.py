
import logging
#12 Hours format with date 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:: %(levelname)s :: %(message)s',datefmt="%d-%m-%y %I:%M:%S %p") 
 
#24 Hours format with date 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:: %(levelname)s :: %(message)s',datefmt="%d-%m-%y %H:%M:%S") 
 
logging.critical("Critical Needs Action immediately") 
logging.error("Error Occured") 
logging.warning("warning") 
logging.info("Some one has logged in !!") 
logging.debug("Debugging Successfull!") 
#logging.notset("notset")