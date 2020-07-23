import PyPDF2
import sys

#grabs all arguments from command line except for first one
inputs = sys.argv[1:]
watermark = "wtr.pdf"

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write("super.pdf")

def pdf_watermark():
	template = PyPDF2.PdfFileReader(open('super.pdf', "rb"))
	watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
	output = PyPDF2.PdfFileWriter()

	for i in range(template.getNumPages()):
		page = template.getPage(i)
		page.mergePage(watermark.getPage(0))
		output.addPage(page)

		with open('watermarked_output.pdf', "wb") as file: 
			output.write(file)

		

pdf_combiner(inputs)
pdf_watermark()