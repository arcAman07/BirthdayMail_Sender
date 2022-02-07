import csv
from csv import writer
# open the file in the write mode
f = open('C:/Users/amans/Downloads/mailingList.csv', 'w')

# create the csv writer
# spamwriter = writer(f)

row = [4,"Tanmay","b@gmail.com"]

# # write a row to the csv file
# spamwriter.writerow(row)

# # close the file
# f.close()

with open(f, 'a') as f_object:
  
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
  
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(row)
  
    #Close the file object
    f_object.close()