#!/usr/bin/python
# -*- coding: utf-8 -*-


import logging


module_logger = logging.getLogger('logging_initialization.bin_file')


def concatenate_files():
    ''' open files and  concatenate '''
    filenames = ['text1.txt', 'text2.txt']
    logger = logging.getLogger('logging_initialization.bin_file.concatenate_file')
    logger.info(' opening text files and concatenating into one')
    with open('text_out.txt', 'w') as outfile:
        for name in filenames:
            with open(name) as infile:

                outfile.write(infile.read().replace('\n', ''))

def convert_concatenated_file():
    ''' converted concatenated file into bytes '''
    logger = logging.getLogger('logging_initialization.bin_file.converted_into_bytes')
    with open('text_out.txt','r') as convertfile:

        encoded_file_into_bytes= bytes(convertfile.readline(), encoding= 'utf-8')
        logger.debug('''type of 'convertfile{}'''.format(type(convertfile)))

        logger.info('converted into bytes concatenated strings in text_out.tex')
        logger.debug('result of convert {}'.format(encoded_file_into_bytes))
        return encoded_file_into_bytes

def wright_bytes_file():
        with open('Result.bin', 'r+b') as resultfile:

            resultfile.write(convert_concatenated_file())




