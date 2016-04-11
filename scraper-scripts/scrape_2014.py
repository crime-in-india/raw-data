import csv
import os

filename = 'crime-table-2014.csv'
FILE_PATH = os.path.join('raw-csv', filename)
year = 2014
crime = ''
city = ''
inc = 0
rate = 0

with open(FILE_PATH, 'r') as f_in:
    datarows = csv.reader(f_in)
    # keys = next(datarows) #get crime names  
    # next(datarows) #skip row with I/R as headers

    with open('2014.csv', 'w') as f_out:
        writer = csv.writer(f_out)
        header = ['city', 'year', 'crime', 'incidences', 'rate']
        writer.writerow(header) #writer header for output file
        
        for row in datarows:
            # Check if we have finished one table and are about to 
            # move on to the next table in the file
            if row[0] == '':
                keys = list(set(next(datarows))) #get crime names
                del keys[0] #Delete first element since it's not a crime
                next(datarows) #skip row with I/R as headers
                
            else:
                #Else read in the row
                city = row[0]
                print('Currently on:', city)

                for k in range(0,len(keys),2):
                    #For each city, get the crime numbers
                    print('Getting data for:', keys[k])
                    crime = keys[k]
                    city = row[0]
                    inc = row[k + 1]
                    rate = row[k + 2]
                    #Write to csv
                    output_row = [city, year, crime, inc, rate]
                    writer.writerow(output_row)