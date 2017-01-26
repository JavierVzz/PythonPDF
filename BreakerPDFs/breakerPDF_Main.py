# Javier Vazquez
# Python 3.6.0

import os
from operationsPDF import PDF_operations

def main():
    print(os.getcwd())
    opPdf = PDF_operations()
    print("Press 1 to encrypt pdf files")
    print("Press 2 to decrypt pdf files")
    print("Press 3 to break password to decrypt pdf files")
    option = input("Option: ")
    option = int(option)
    if option == 1:
        # password = opPdf.passwordGenerator()
        password = opPdf.passwordDictionary()
        print("Password: ", password)
        opPdf.encrypting(password)
    elif option == 2:
        password = input("Password: ")
        opPdf.unEncrypting(password)
    elif option == 3:
        opPdf.dictCodeBreaker()
    else:
        print("Incorrect input")

    input("Press [enter] to exit!")


if __name__ == '__main__':
    main()
