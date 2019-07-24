#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Author: Shieber
#    Date: 2019.06.22
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
#    split a pdf with start page number and last page number parameters.
#
#    Copyright 2019 
#    All Rights Reserved!

import sys
import PyPDF2

class PDFCuter():
    '''分割pdf'''
    def __init__(self,inputs,output,start,end):
        self.origin = inputs
        self.output = output 
        self.start  = start
        self.end    = end

    def newpdf(self):
        '''pdf'''
        with open(self.origin,'rb') as pdfObj:
            pdfReader = PyPDF2.PdfFileReader(pdfObj)

        maxm = pdfReader.numPages
        if not (1<= abs(self.start) <=maxm): #页数不在范围内，退出
            print("Error, your page number is not valid!")
            sys.exit(-1)

        pdfWriter = PyPDF2.PdfFileWriter()
        if self.start <0 and self.end <0:
            pageObj = pdfReader.getPage(self.start) 
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

        with open(self.output,'wb') as outputObj:
            pdfWriter.write(outputObj)

if __name__ == "__main__":
    argv = sys.argv
    lnth = len(argv)
    if lnth == 3:
        start,end = 1,1
    elif lnth == 4:
        start,end = int(argv[3]),int(argv[3])
    elif lnth == 5:
        start,end = int(argv[3]),int(argv[4])
    else:
        print('Usage: pdfcut file.pdf output.pdf (start) (end)')
        sys.exit(-1)

    pdfname  = argv[1]
    output   = argv[2]
    pdfcuter = PDFCuter(pdfname, output, start, end)
    pdfcuter.newpdf()
