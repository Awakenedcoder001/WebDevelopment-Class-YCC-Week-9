#Second program: 
import logging
logger=logging.getLogger("sentry") 
 
try: 
 file_read=open("writing10.txt") 
 contents=file_read.read() 
 print(contents) 
 
 result=10/2
 
except FileNotFoundError as msg: 
 logger.error(msg) 
  
except ZeroDivisionError as msg: 
 logger.error(msg) 
 logger.info("Cannot Be Divided By Zero")