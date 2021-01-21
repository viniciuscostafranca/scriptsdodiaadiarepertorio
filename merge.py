
import os, PyPDF2


userpdflocation=input( 'Caminho onde o pdf se encontra:  ')


os.chdir(userpdflocation)

userfilename=input( 'Como você gostaria de chamar o arquivo ')


pdf2merge = []
for filename in os.listdir( '.'):
    if filename.endswith( '.pdf'):
        pdf2merge.append(filename)

pdfWriter = PyPDF2.PdfFileWriter()


for filename in pdf2merge:
    #rb for read binary
    pdfFileObj = open(filename,  'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Opening each page of the PDF   
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
#save PDF to file, wb for write binary
pdfOutput = open(userfilename+  '.pdf  ',  'wb')
#Outputting the PDF
pdfWriter.write(pdfOutput)
#Closing the PDF writer
pdfOutput.close()