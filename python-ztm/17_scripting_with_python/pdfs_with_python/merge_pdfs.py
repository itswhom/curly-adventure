import PyPDF2
import sys

# take arguments: pdf to modify, pdf containing watermark

# apply second argument as watermark

# save pdf 

# 

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)