# Javier Vazquez
# Python 3.6.0

import sys, re, os, PyPDF2, pprint
from operationsPDF import PDF_operations

def main():
    opPdf = PDF_operations()
    opPdf.listPDFs()
    opPdf.combining()

if __name__ == '__main__':
    main()