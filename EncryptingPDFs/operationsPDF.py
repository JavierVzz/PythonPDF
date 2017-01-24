# Javier Vazquez
# Python 3.6.0
# version 2.0 -- encrypting option added
# Jan 23, 2017

import sys, re, os, PyPDF2, pprint

class PDF_operations():

    def __init__(self):
        pass

    def listPDFs(self, encrypted):
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
        listPDFs = self.listPDFs(False)
        for pdf in listPDFs:
            print(pdf)
        for i in range(len(listPDFs)):
            pdfFile = open(listPDFs[i], "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            #pdfReader = PyPDF2.PdfFileReader(open(listPDFs[i], "rb"))
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
            pdfOutputFile = open("encrypted_"+listPDFs[i], "wb")
            pdfWriter.encrypt(password)
            pdfWriter.write(pdfOutputFile)
            pdfOutputFile.close()
            pdfFile.close()
        self.deleteUnencrypted()

    def deleteUnencrypted(self):
        listPDFs = self.listPDFs(False)
        for pdf in listPDFs:
            os.remove(pdf)

    def combining(self):
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