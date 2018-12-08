#!/usr/bin/env python
"""
   Please note: this script works with python 3 only
   All backup are saved in the user home dir under backup dir:
       /home/username/backup/
"""

import csv
import subprocess
import pexpect             # to work must install: sudo apt-get install python3-pexpect
from func import *
from pathlib import Path
#from scp import SCPClient  # to work must install: sudo apt-get install python3-scp
#import paramiko            # to work must install: sudo apt-get install python3-paramiko


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
            home_dir = str(Path.home())
            backup_dir = home_dir+"/backup/"+company+"/"+serial+"/"
            temp_dir = home_dir+"/backup/tmp/"
            valdir = validate_dir(backup_dir)
            valdir = validate_dir(temp_dir)
            connection = user+"@"+ip+":fgt-config"
            connect = pexpect.spawn('scp -o StrictHostKeyChecking=no %s %s' % (connection, temp_dir))
            connect.expect("password:")
            connect.sendline(upass)
            connect.expect(pexpect.EOF, timeout=10)

