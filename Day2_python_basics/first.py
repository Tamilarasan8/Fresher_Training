import logging
n=input("enter n value:")
logging.basicConfig(filename = 'file.txt',
                    level = logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s',filemode='w')

logging.error("error")
logging.critical("critical")
logging.debug("debugging")
logging.info("info ")
logging.warning("warning")
try:
    1*n
except:
    logging.error("error from except",exc_info=0)