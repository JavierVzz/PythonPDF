# Javier Vazquez
# Python 3.6.0

import os
from operationsPDF import PDF_operations

def main():
    print(os.getcwd())
    opPdf = PDF_operations()
    for pdf in opPdf.listPDFs():
        print(pdf)
    opPdf.combining()

if __name__ == '__main__':
    main()