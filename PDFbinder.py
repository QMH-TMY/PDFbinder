#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Author: Shieber
#    Date: 2019.07.24
#
import sys, PyPDF2
from os.path import basename

class PDFcombiner():
    '''pdf文件合并类'''
    def __init__(self):
        self.pdflist = sys.argv[1:] 	#获取命令行输入的pdf文件存储为列表
        self.pdfnums = len(sys.argv)  	#获取命令行输入参数个数
        self.output  = sys.argv[-1] 	#输出文件名
        self.program = basename(sys.argv[0])

    def _ispdf(self):
        '''判断输入文件是否全为pdf'''
        for pdf in self.pdflist:
            if not pdf.endswith('.pdf'):
                return False          	#只要有一个不是pdf后缀就退出
        return True

    def _add_pdf_pages(self):
        '''向writer中添加pdf页数'''
        if not self._ispdf():
            print("Files are invalid .")
            sys.exit(-1)

        pdfWriter = PyPDF2.PdfFileWriter()
        for pdf in self.pdflist[1:-1]:
            pdfReader = PyPDF2.PdfFileReader(open(pdf,'rb'))
            for page in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(page)
                pdfWriter.addPage(pageObj)

        return pdfWriter

    def combine(self):
        '''合并写入'''
        if self.pdfnums < 4:
            print(f"Usage: {self.program} s1.pdf s2.pdf ... output.pdf")
            sys.exit(-1)

        pdfWriter = self._add_pdf_pages()
        with open(self.output,'wb',encoding='utf-8') as pdfObj:
            pdfWriter.write(pdfObj)

if __name__ == "__main__":
    pdfcombiner = PDFcombiner()
    pdfcombiner.combine()
