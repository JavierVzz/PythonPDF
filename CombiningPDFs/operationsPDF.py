# Javier Vazquez
# Python 3.6.0

import sys, re, os, PyPDF2, pprint

class PDF_operations():

    def __init__(self):
        pass

    def listPDFs(self):
        listPdfs = []
        extRegex = re.compile(r".+pdf$")
        listFiles = os.listdir()
        for file in listFiles:
            ext = extRegex.search(file)
            if ext is not None:
                listPdfs.append(ext.group())
        print(os.getcwd())
        # for pdf in listPdfs:
        #     print(pdf)
        return listPdfs

    def combining(self):
        pprint.pprint(self.listPDFs())
        for pdf in self.listPDFs():
            pdfFile = open(pdf, "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

        pdfFinal = open("combined.pdf", "wb")
        pdfWriter.write(pdfFinal)
        pdfFinal.close()




if __name__ == '__main__':
    print("Direct access to "+ os.path.basename(__file__))
else:
    print(os.path.basename(__file__)+" class instance")