# Javier Vazquez
# Python 3.6.0
# version 2.0 -- encrypting option added
# Jan 23, 2017

import re, os, PyPDF2, random, string, sys

class PDF_operations():

    def __init__(self):
        pass

    def listPDFs(self, encrypted):
        '''Lists the pdf files that are or are not encrypted,
        True encrypted, False not encryted'''
        pdfList = []
        extRegex = re.compile(r".+pdf$")
        listFiles = os.listdir()
        for file in listFiles:
            ext = extRegex.search(file)
            if ext is not None:
                if encrypted == False:
                    pdfFile = open(ext.group(), "rb")
                    pdfReader = PyPDF2.PdfFileReader(pdfFile)
                    pdfFile.close()
                    if pdfReader.isEncrypted == False:
                        pdfList.append(ext.group())
                elif encrypted == True:
                    pdfFile = open(ext.group(), "rb")
                    pdfReader = PyPDF2.PdfFileReader(pdfFile)
                    pdfFile.close()
                    if pdfReader.isEncrypted == True:
                        pdfList.append(ext.group())
        pdfList.sort()
        return pdfList

    def encrypting(self, password):
        '''Encrypts pdf files'''
        listPDFs = self.listPDFs(False)
        for pdf in listPDFs:
            print(pdf)
        for i in range(len(listPDFs)):
            pdfFile = open(listPDFs[i], "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
            pdfOutputFile = open("encrypted_"+listPDFs[i], "wb")
            pdfWriter.encrypt(password)
            pdfWriter.write(pdfOutputFile)
            pdfOutputFile.close()
            pdfFile.close()
        self.deletePDFs(encrypted= False)

    def unEncrypting(self, password):
        '''Decrypts pdf files'''
        j = 0
        listPDFs = self.listPDFs(True)
        for pdf in listPDFs:
            print(pdf)
        for i in range(len(listPDFs)):
            pdfFile = open(listPDFs[i], "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.decrypt(password) == 0:
                print("Wrong password!!!")
                pdfFile.close()
                break
            else:
                j += 1
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                listPDFs[i] = listPDFs[i].replace("encrypted_","")
                pdfOutputFile = open(listPDFs[i], "wb")
                pdfWriter.write(pdfOutputFile)
                pdfOutputFile.close()
                pdfFile.close()
        if j == len(listPDFs):
           self.deletePDFs(encrypted=True)

    def dictCodeBreaker(self):
        '''Decrypts pdf files'''
        j = 0
        password = ""
        listPDFs = self.listPDFs(True)
        for pdf in listPDFs:
            print(pdf)

        dictionary = open("dictionary.txt", "r")
        words = dictionary.readlines()
        dictionary.close()
        pdfFile = open(listPDFs[0], "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        for word in words:
            if pdfReader.decrypt(word.replace("\n", "")) == 1:
                print("Password: ",word)
                password = word.replace("\n", "")
                pdfFile.close()
                break
        for i in range(len(listPDFs)):
            pdfFile = open(listPDFs[i], "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.decrypt(password) == 0:
                print("Wrong password!!!")
                pdfFile.close()
                break
            else:
                j += 1
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                listPDFs[i] = listPDFs[i].replace("encrypted_","")
                pdfOutputFile = open(listPDFs[i], "wb")
                pdfWriter.write(pdfOutputFile)
                pdfOutputFile.close()
                pdfFile.close()
        if j == len(listPDFs):
           self.deletePDFs(encrypted=True)

    def deletePDFs(self, encrypted):
        '''Deletes pdf files that are or are not encrypted,
        True encrypted, False not encrypted'''
        listPDFs = self.listPDFs(encrypted)
        for pdf in listPDFs:
            os.remove(pdf)

    def passwordGenerator(self):
        '''Generates a random password of 4 characters long'''
        chars = string.ascii_letters + string.digits
        password = ""
        for i in range(4):
            password += chars[random.randint(0, len(chars))]
        return password

    def passwordDictionary(self):
        '''Takes as password one word from the dictionary.txt file'''
        dictionary = open("dictionary.txt", "r")
        words = dictionary.readlines()
        dictionary.close()
        return words[random.randint(0, len(words)-1)].replace("\n","")

    def combining(self):
        '''Combines several pdfs files, only the first one keeps its cover'''
        outputFile = "combined.pdf"
        if os.path.isfile(outputFile) is True:
            os.remove(outputFile)
        listPDFs = self.listPDFs()
        for i in range(len(listPDFs)):
            pdfFile = open(listPDFs[i], "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if i == 0:
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
            else:
                for pageNum in range(pdfReader.numPages):
                    if pageNum != 0:
                        pageObj = pdfReader.getPage(pageNum)
                        pdfWriter.addPage(pageObj)

                if i == len(listPDFs) - 1:
                    pdfFinal = open(outputFile, "wb")
                    pdfWriter.write(pdfFinal)
                    pdfFinal.close()


if __name__ == '__main__':
    print("Direct access to "+ os.path.basename(__file__))
else:
    print(os.path.basename(__file__)+" class instance")