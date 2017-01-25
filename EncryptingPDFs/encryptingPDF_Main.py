# Javier Vazquez
# Python 3.6.0

import os
from operationsPDF import PDF_operations

def main():
    print(os.getcwd())
    opPdf = PDF_operations()
    # for pdf in opPdf.listPDFs(False):
    #     print(pdf)
    #password = input("Password: ")
    #opPdf.unEncrypting(password)
    opPdf.passwordGenerator()


if __name__ == '__main__':
    main()