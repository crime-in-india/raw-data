
from csv import writer
from glob import glob
from xlrd import open_workbook
from os.path import splitext, basename
for fname in glob('*.xlsx'):
    _x, _xt = splitext(fname)
    cname = _x + '.csv'
    print("writing to", cname)
    cf = open(cname, 'w')
    cv = writer(cf)
    book = open_workbook(fname)
    sheet = book.sheets()[0]
    for n in range(sheet.nrows):
        rowvals = sheet.row_values(n)
        cv.writerow(rowvals)
    cf.close()