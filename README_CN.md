### 兼容系统  
- Linux 
- Mac OS
- Windows

### PDFbinder & PDFcuter 
[[English](./README.md)] 命令行pdf文件合并和分割器。

### 依赖
	PyPDF2 
    $ sudo pip install PyPDF2

### 合并 
    # python PDFbinder.py s1.pdf s2.pdf ... output.pdf 合并多个文件到output.pdf

### 分割 
    # python PDFcuter.py input.pdf output.pdf start end 分割start到end页到output.pdf
    $ python PDFcuter.py input.pdf output.pdf 1 4

### 我问你资不资持？
![payment](./payment.png)

