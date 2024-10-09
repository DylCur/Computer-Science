import csv

data = [
    ['Name', 'Branch', 'Year', 'CGPA'],
    ['Nikhil', 'COE', 2, 9.0],
    ['Sanchit', 'COE', 2, 9.1],
    ['Aditya', 'IT', 2, 9.3],
    ['Sagar', 'SE', 1, 9.5],
    ['Prateek', 'MCE', 3, 7.8],
    ['Sahil', 'EP', 2, 9.1]
]

with open('university_records.csv', 'w+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
