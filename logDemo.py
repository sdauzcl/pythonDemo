import logging
# logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d %X')
# logging.info(' info logging')
# logging.debug('debug logging')
# logging.warning('warning logging')
# logging.error('error logging')
# logging.critical('critical logging')


logging.basicConfig(filename='test.log',format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)
logging.debug('debug 信息')
logging.info('info 信息')
logging.warning('warning 信息')
logging.error('error 信息')
logging.critical('critial 信息')
