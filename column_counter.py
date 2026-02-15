import csv

file_name="practice_data.csv"

with open(file_name,"r") as file:
    reader=csv.reader(file)         #converts data in the form of list(each row)
    first_row=next(reader)          #To get only first row
    print("No.of columns: ",len(first_row))