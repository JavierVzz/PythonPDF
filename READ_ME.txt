PDF_operations()
The following program class is contained in the [operationsPDF.py] file.
PDF_operations() class has the following methods:
* __init__
o constructor
* listPDFs
o Displays all the pdf files in the current work directory
* encrypting
o Encrypts all the decrypted pdf files in a new pdf file with the same name just adding encrypted_ at the beginning of the file name.
o Deletes all the decrypted pdf files after encrypting them.
* unEncrypting
o Decrypts all the encrypted pdf files in a new pdf file with the same name just removing the prefix encrypted_ at the beginning of the file name.
o Deletes all the decrypted pdf files after encrypting them.
* deletePDFs
o Deletes the pdf files that are or are not encrypted, according to the parameter encrypted
* True: deletes encrypted pdf files.
* False: deletes decrypted pdf files.
* PasswordGenerator
o Generates a random password of 4 characters long
* combining
o Deletes the [combined.pdf] file if already exists. 
o Combines all the pdf files listed by ListPDFs method into the [combined.pdf] file


