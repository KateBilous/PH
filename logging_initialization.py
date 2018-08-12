#!/usr/bin/python
# -*- coding: utf-8 -*-


import logging
import bin_file


def main():
    '''The main entry point of the application
    '''


#logging.basicConfig(filename=u'log_file.log')
# logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO, filename=u'logfile.log')

logger = logging.getLogger('logging_initialization')
logger.setLevel(logging.DEBUG)

# create logging file handler
fh = logging.FileHandler('log_file.log')

formatter = logging.Formatter(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
fh.setFormatter(formatter)

# add handler to logger object
logger.addHandler(fh)
logging.info('Program started')
bin_file.concatenate_files()
#bin_file.convert_concatenated_file()
bin_file.wright_bytes_file()
logging.info('Done!')

if __name__ == '__main__':
    main()
