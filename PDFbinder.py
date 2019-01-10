#!/usr/bin/python
# -*- coding: utf-8 -*-
# 合并多个pdf为一个

import sys, PyPDF2
from os.path import basename

class PDFcombiner():
	'''pdf文件合并类'''
	def __init__(self):
		self.pdflist = sys.argv[1:-1] 	#获取命令行输入的pdf文件存储为列表
		self.pdfnums = len(sys.argv)  	#获取命令行输入的pdf文件个数
		self.outputname = sys.argv[-1] 	#输出文件名

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
			for pdf in self.pdflist:
				pdfReader = PyPDF2.PdfFileReader(file(pdf,'rb'))
				for page in range(pdfReader.numPages):
					pageObj = pdfReader.getPage(page)
					pdfWriter.addPage(pageObj)
			return pdfWriter

		else:
			print("Files are not valid pdf file")
			sys.exit(-1)

	def pdfcombine_main(self):
		'''合并写入'''
		if self.pdfnums < 4:
			print("Usage: %s [s1.pdf] [s2.pdf] ... [output.pdf]"%basename(sys.argv[0]))
			sys.exit(-1)

		pdfWriter = self.addpdfpages()
		
		if self.outputname.endswith('.pdf'):
			pdfOutPut = open(self.outputname,'wb')
		else:
			pdfOutPut = open(self.outputname + '.pdf','wb')

		pdfWriter.write(pdfOutPut)
		pdfOutPut.close()

if __name__ == "__main__":
	pdfcombiner = PDFcombiner()
	pdfcombiner.pdfcombine_main()
