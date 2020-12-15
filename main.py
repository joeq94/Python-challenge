# Libraries 
import os
import csv

# os.path.join() is a function that ask to get the address of the file
pyBank_data = os.path.join("Resources","") 

# setting a variable
totalAmount = 0
totalMonths = 0
#this line just opens the file
#while the pybank file is open
with open(pyBank_data) as data:
    #read the file 
    csvReader = csv.reader(data,delimiter=',')
    # we need to tell the loop to skip the first row
    header = next(csvReader)
    #for every row in the file
    for row in csvReader:
        # totalMonths += 1
        # 1 = 0 + 1
        totalMonths = totalMonths +1
        # totalAmount(new) = totalAmount(old) +row
        totalAmount = totalAmount + int(row[1])
    print("Total Months:",totalMonths)
    print("Total Amount:", totalAmount) # <- it has to do with this line