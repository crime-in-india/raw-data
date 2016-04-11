import pdfplumber
import csv

pdf_name = 'raw-pdfs/crime-stats-2013.pdf'
pdf = pdfplumber.open(pdf_name)

page = pdf.pages[32]
table = page.extract_table()

with open('2013.csv', 'w') as outfile:
	outcsv = csv.writer(outfile)

	for row in table:
		outcsv.writerow(row)