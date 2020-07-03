import PyPDF2 as Py
fname='C:\\Users\\piyus\\Downloads\\The_Living_World.pdf'
pdffile=open(fname,'rb')
pdfread=Py.PdfFileReader(pdffile)

for i in range(pdfread.getNumPages()):
    print('-----------------Page Number {}------------------------'.format(i+1))
    pageinfo=pdfread.getPage(i)
    print(pageinfo.extractText())

pdffile.close()
