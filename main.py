from book.exception import BookException
from book.logger import logging
import os,sys

if __name__=='__main__':
    try:
        pass
    except Exception as e:
        raise BookException(e,sys)
