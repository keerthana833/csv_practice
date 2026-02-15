import csv

file_name="practice_data.csv"

number_courses=input("Enter no.of courses: ")
time_study=input("Enter study time: ")
new_marks=input("Enter marks: ")

with open(file_name,"a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow([number_courses,time_study,new_marks])


print("Data updated successfully")