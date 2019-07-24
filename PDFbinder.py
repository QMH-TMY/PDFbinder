#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#    Author: Shieber
#    Date: 2019.07.24
#
#                             APACHE LICENSE
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
#                            Function Description
#    transfer txt file to pdf file.
#    combine multiple pdf files into sigle one pdf.
#
#    Copyright 2019 
#    All Rights Reserved!

import sys, PyPDF2
from os.path import basename

class PDFcombiner():
    '''pdf文件合并类'''
    def __init__(self):
        self.pdflist = sys.argv[1:] 	#获取命令行输入的pdf文件存储为列表
        self.pdfnums = len(sys.argv)  	#获取命令行输入参数个数
        self.output  = sys.argv[-1] 	#输出文件名
        self.program = basename(sys.argv[0])

    def ispdf(self):
        '''判断输入文件是否全为pdf'''
        for pdf in self.pdflist:
            if not pdf.endswith('.pdf'):
                return False          	#只要有一个不是pdf后缀就退出
        return True

    def addpdfpages(self):
        '''向writer中添加pdf页数'''
        if self.ispdf():
            pdfWriter = PyPDF2.PdfFileWriter()
            for pdf in self.pdflist[1:-1]:
                pdfReader = PyPDF2.PdfFileReader(file(pdf,'rb'))
                for page in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(page)
                    pdfWriter.addPage(pageObj)
            return pdfWriter
        else:
            print("Files are not valid pdf file")
            sys.exit(-1)

    def combine(self):
        '''合并写入'''
        if self.pdfnums < 4:
            print("Usage: %s s1.pdf s2.pdf ... output.pdf"%self.program)
            sys.exit(-1)

        pdfWriter = self.addpdfpages()
        with open(self.output,'wb') as pdfObj:
            pdfWriter.write(pdfObj)

if __name__ == "__main__":
    pdfcombiner = PDFcombiner()
    pdfcombiner.combine()
