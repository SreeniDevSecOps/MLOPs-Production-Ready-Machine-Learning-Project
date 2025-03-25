from us_visa.logger import logging
from us_visa.exception import USvisaException

# logging.info("This is a test message")
 
try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)