# Javier Vazquez
# Python 3.6.0

import sys, re, os, PyPDF2

class PDF_operations():

    def __init__(self):
        pass

    def listFiles(self):
        pass

if __name__ == '__main__':
    print("Direct access to "+ os.path.basename(__file__))
else:
    print(os.path.basename(__file__)+" class instance")