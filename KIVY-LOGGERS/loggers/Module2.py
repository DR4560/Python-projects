#Module2.py
import logging


module_logger =logging.getLogger("SampleApp.Module2")

def add(y,x):
    logger = logging.getLogger("SampleApp.Module2.add")
    logging.info("The commit edited: added %s .block and %s .string to the file %s" % (x,y, 'summary.txt'))
    return 'summary.txt'

