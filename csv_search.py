import csv

file_name="practice_data.csv"
search_marks=float(input("Enter marks to search: "))

with open(file_name,"r") as file:
    reader=csv.reader(file)
    next(reader)

    found=False
    for row in reader:
        if float(row[2])==search_marks:
            found=True
            break

if found:
    print("Found")
else:
    print("Not Found")