#!/usr/bin/env python

import csv
from func import *


print("Current path: " ,os.getcwd())
print("Relative path: " ,relative_path("data.csv") ,"\n")



with open(relative_path("data.csv")) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # Skip first line
    for row in csv_reader:
          #print(row)
          #print(", ".join(row))
        company = row[0]
        user = row[1]
        upass = row[2]
        ip = validate_ip(row[3])
        
        print(company, user, upass, ip)
        
