import sentry_sdk 
import logging 
 
sentry_sdk.init( 
    "https://84c733eecc6245dbb556e8010163eff4@o1078188.ingest.sentry.io/6081761", 
 
    # Set traces_sample_rate to 1.0 to capture 100% 
    # of transactions for performance monitoring. 
    # We recommend adjusting this value in production. 
    traces_sample_rate=1.0 
) 
 
#=logging.getLogger("sentry") 
logging.basicConfig(filename="log.txt",level=logging.DEBUG,format="%(asctime)s %(levelname)s") 
 
try: 
 file_read=open("writing10.txt" ) 
 contents=file_read.read() 
 print(contents) 
 
 result=10/0 
 
except FileNotFoundError as msg: 
 #logger.error(msg) 
 logging.error(msg) 
 
except ZeroDivisionError as msg: 
 logging.error(msg) 
 logging.info("Cannot Be Divided By Zero")

 