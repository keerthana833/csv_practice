import csv

input_file="practice_data.csv"
output_file="high_marks.csv"

with open(input_file,"r") as rfile,open(output_file,"w",newline="") as wfile:
    # Reads csv row by row
    reader=csv.reader(rfile)  
    # Writes rows into new csv file     
    writer=csv.writer(wfile)        



    for i,row in enumerate(reader):
        if i==0:
            writer.writerow(row)
            print(row)
        else:
                if float(row[2])>=30:
                     writer.writerow(row)
                     print(row)
                     
                    



