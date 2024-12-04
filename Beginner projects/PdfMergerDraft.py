"""PDF MERGER INTO A SINGLE FILE """
#enhancing by a few code lines efficiency
#simplifies file management as well


import PyPDF2
import sys

import openpyxl.utils.units

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger = PyPDF2.PdfFileMerger()
        merger.append(file)
    merger.write("combined")

######other way*
files = ["/home/vially/WORK/osw/file1.pdf", "/home/vially/WORK/osw/file2.pdf"]
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
        print(file)

merger.write("MainFile.pdf")

nano open.sh
zsh open.sh "<link>"


#!/bin/zsh
cd C:\Users\Patri\PycharmProjects\6projects
python3 main.py $1