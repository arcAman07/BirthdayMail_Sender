import csv

# open the file in the write mode
f = open('C:/Users/amans/Downloads/mailingList.csv', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(row)

# close the file
f.close()
