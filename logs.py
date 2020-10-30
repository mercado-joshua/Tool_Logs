#===========================
# Imports
#===========================

import logging as lg

#===========================
# Main Script
#===========================

class Log:
    def __init__(self, name=__name__):
        self.__logger = lg.getLogger(name)

    def level(self, level=lg.DEBUG):
        self.__logger.setLevel(level)
        return self

    def consolehandler(self):
        self.__handler = lg.StreamHandler()
        return self

    def filehandler(self, filepath='test.log'):
        self.__handler = lg.FileHandler(filepath)
        return self

    def formatter(self, format_='%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s'):
        self.__handler.setFormatter(lg.Formatter(format_))
        self.__logger.addHandler(self.__handler)
        return self

    def disable_log(self, level=lg.CRITICAL):
        lg.disable(level)

    def exception(self, message):
        self.__logger.exception(message)

    def debug(self, message):
        self.__logger.debug(message)

    def info(self, message):
        self.__logger.info(message)

    def warning(self, message):
        self.__logger.warning(message)

    def error(self, message):
        self.__logger.error(message)

    def critical(self, message):
        self.__logger.critical(message)


#===========================
# Start Program
#===========================

def main():
    pass
    ## 1
    # log = Log()
    # log.level()
    # log.consolehandler().formatter()
    # log.filehandler('huhuhu.log').formatter()
    # # log.disable_log()

    # log.debug('Start of Program')
    # log.debug('Some debugging details.')
    # log.info('The logging module is working.')
    # log.warning('An error message is about to be logged.')
    # log.error('An error has occurred.')
    # log.critical('The program is unable to recover!')
    # log.debug('End of Program')

    ## 2
    # log = Log()
    # log.level()
    # log.consolehandler().formatter()
    # # log.disable_log()

    # log.debug('Start of Program')
    # log.debug('Some debugging details.')
    # log.info('The logging module is working.')
    # log.warning('An error message is about to be logged.')
    # log.error('An error has occurred.')
    # log.critical('The program is unable to recover!')
    # log.debug('End of Program')

    ## 3
    # log = Log()
    # log.level()
    # log.filehandler('huhuhu.log').formatter()
    # # log.disable_log()

    # log.debug('Start of Program')
    # log.debug('Some debugging details.')
    # log.info('The logging module is working.')
    # log.warning('An error message is about to be logged.')
    # log.error('An error has occurred.')
    # log.critical('The program is unable to recover!')
    # log.debug('End of Program')

    # try:
    #     out = 5 / 0
    # except ZeroDivisionError:
    #     log.exception('Division by zero')
    # else:
    #     return out

if __name__ == '__main__':
    main()