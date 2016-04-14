import csv
from glob import glob
import os

all_files = glob('../raw-csv/abbyy/csv/20*.csv')
master = []
output_file = 'master.csv'

for f in all_files:
    thefile = os.path.basename(f)
    the_path = folder_path + thefile

    print('Currently on', thefile)
    year = thefile[:4] #extract year from each file name
    
    with open(f, 'r') as csv_in:

        datarows = csv.reader(csv_in)
        keys = next(datarows)
        city = ''
        inc = 0
        rate = 0
        crime = ''

        for row in datarows:
            city = row[0]
            print('Currently on city', city, 'in year', year)

            for k in range(1, len(keys), 2):
                if keys[k] is not '' or keys[k] is not 'City':
                    crime = keys[k]
                    inc = row[k]
                    rate = row[k+1]
                    output_row = [city, year, crime, inc, rate]
                    master.append(output_row)

with open(output_file, 'w') as csv_out:
    writer = csv.writer(csv_out)
    header = ['city', 'year', 'crime', 'incidences', 'rate']
    writer.writerow(header) #writer header for output file

    for r in master:
        writer.writerow(r)