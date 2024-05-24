import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

filepath = input("which directory are the files in?: ")
os.chdir(filepath)

for file in os.listdir():
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("Combined.pdf")
