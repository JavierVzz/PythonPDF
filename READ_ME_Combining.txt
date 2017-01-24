Combining PDFs
The following program combines several pdf files into a single pdf [combined.pdf]. Only the first pdf file has a cover, for the following pdf files the cover has been removed. The pdf files are sorted in alphabetical order.
Scripts:
* combiningPDF_Main.py - main function:
o Creates an instance of PDF_operations()

* operationsPDF.py - PDF_operations() class with the following methods:
o __init__
* constructor
o ListPDFs
* Displays all the pdf files in the current work directory
o Combining
* Erase the [combined.pdf] file if already exists. 
* Combines all the pdf files listed by ListPDFs method into the [combined.pdf] file

