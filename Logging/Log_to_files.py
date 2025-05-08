import logging

logging.basicConfig(level=logging.DEBUG, filemode='w', filename='MainLog.log',
                    format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s')

class logtofile:
    @staticmethod
    def debug(text):
        logging.debug(text)

    @staticmethod
    def info(text):
        logging.info(text)


