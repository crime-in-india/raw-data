"""
This code processes each xlsx file in the xlsx/* path,
 then writes the data (a list of values) to CSV files stored in the csv/ path

The CSVs are all stored in the same subdirectory, with this naming pattern:

YEAR-page_PGNUM.csv

"""

from csv import writer
from glob import glob
from os.path import basename, join
from os import makedirs
from xlrd import open_workbook
import re

CSV_DIRNAME = 'csv'
makedirs(CSV_DIRNAME, exist_ok=True)

for xfname in glob(join('xlsx', '*', '*.xlsx')):
    yr, pg_num = re.search(r'(\d{4}) - (\d{4})', basename(xfname)).groups()
    cname = join(CSV_DIRNAME, '{year}-page_{page}.csv'.format(year=yr, page=pg_num))
    print("writing to", cname)
    cf = open(cname, 'w')
    cv = writer(cf)
    book = open_workbook(xfname)
    sheet = book.sheets()[0]
    for n in range(sheet.nrows):
        rowvals = sheet.row_values(n)
        cv.writerow(rowvals)
    cf.close()
