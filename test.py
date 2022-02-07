import csv

# open the file in the write mode
f = open('C:/Users/amans/Downloads/mailingList.csv', 'w')

# create the csv writer
spamwriter = csv.writer(f)

row = [4,"Tanmay","b@gmail.com"]

# write a row to the csv file
spamwriter.writerow(row)

# close the file
f.close()
