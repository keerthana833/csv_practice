import csv

file_name="practice_data.csv"

with open(file_name,"r") as file:
    reader=csv.reader(file)         #converts data in the form of list(for each row)


    count=0
    for row in reader:
        count+=1

print("Total rows: ",count)

