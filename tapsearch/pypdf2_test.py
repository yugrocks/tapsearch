import PyPDF2

def read_pdf(stream):
    #pdfFileObj = open(filepath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(stream)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    return pageObj.extractText()
