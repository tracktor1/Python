#!/usr/bin/env python

""" Please note: this script works with python 3 only """

import csv
import subprocess
from func import *


print("Current path: " ,os.getcwd())
print("Relative path: " ,relative_path("data.csv") ,"\n")



with open(relative_path("data.csv")) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # Skip first line
    for row in csv_reader:
        company = row[0]
        user = row[1]
        upass = row[2]
        ip = validate_ip(row[3])
        print(company, user, upass, ip)
        if ip == "Invalid IP":
            print("Invalid IP", row[3])
        else:
            subprocess.call(["ping", "-c 1", ip])
            
        
        
