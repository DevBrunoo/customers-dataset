import csv

with open ("Customers.csv", "r") as file: 
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
    
    
