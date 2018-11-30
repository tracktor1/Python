#!/usr/bin/env python
"""
   Please note: this script works with python 3 only
   
   All backup are saved in the user home dir under backup dir
   /home/username/backup/
"""

import csv
import subprocess
from func import *
from pathlib import Path

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
        port = row[4]
        dtype = row[5]
        serial = row[6]
        print(company, user, upass, ip, port, dtype, serial)
        if ip == "Invalid IP":
            print("Invalid IP", row[3])
        else:
            home = str(Path.home())
            backup_dir = home+"/backup/"+company+"/"+serial+"/"
            valdir = validate_dir(backup_dir)
            print(valdir)
            connection = user+"@"+ip+":fgt-config"
            subprocess.call(["scp", "-o StrictHostKeyChecking=no", connection, backup_dir])
            # need to insert password automaticly to continue
