#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 指定起始页分割pdf
# Date: 2019.06.22
# Author: Shieber

import sys
import PyPDF2

class PDFCuter():
    '''分割pdf'''
    def __init__(self,inputfl,outputfl,start,end):
        self.origin = inputfl
        self.output = outputfl 
        self.start  = start
        self.end    = end

    def newpdf(self):
        '''pdf'''
        pdfObj    = open(self.origin,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfObj)
        maxmum    = pdfReader.numPages
        if not (1 <= abs(self.start) <= maxmum):
            pdfObj.close() #页数不在范围内，关闭并退出
            print("Error, your page number is not valid!")
            return None

        pdfWriter = PyPDF2.PdfFileWriter()
        if self.start <0 and self.end <0:
            pageObj = pdfReader.getPage(self.start) #(maxmumpage+self.start)
            pdfWriter.addPage(pageObj)
        elif self.end < 0: 
            self.end += maxmum + 1
            for page in range(self.start-1,self.end):
                pageObj = pdfReader.getPage(page)
                pdfWriter.addPage(pageObj)
        elif self.start == self.end: 
            pageObj = pdfReader.getPage(self.start-1)
            pdfWriter.addPage(pageObj)
        else:
            for page in range(self.start-1,self.end):
                pageObj = pdfReader.getPage(page)
                pdfWriter.addPage(pageObj)

        outputObj = open(self.output,'wb')
        pdfWriter.write(outputObj)
        outputObj.close()
        pdfObj.close() 

if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)
    if length == 3:
        start,end = 1,1
    elif length == 4:
        start,end = int(argv[3]),int(argv[3])
    elif length == 5:
        start,end = int(argv[3]),int(argv[4])
    else:
        print('Usage: pdfcut file.pdf output.pdf (start) (end)')
        sys.exit(-1)


    pdfname  = argv[1]
    output   = argv[2]
    pdfcuter = PDFCuter(pdfname, output, start, end)
    pdfcuter.newpdf()
