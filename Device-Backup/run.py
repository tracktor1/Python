#!/usr/bin/env python
"""
    Please note: this script works with python 3 only
    All backup are saved in the users home dir under backup dir:
        /home/username/backup/device_serial
    run it as:
        python3 ./1.py
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
    next(csv_reader) # Skips the first line in csv file
    for row in csv_reader:
        company = row[0]
        user = row[1]
        upass = row[2]
        ip = validate_ip(row[3])
        port = validate_cell(row[4])
        dtype = row[5]
        serial = row[6]
        print(company, user, upass, ip, port, dtype, serial)
        if ip == "Invalid IP":
            print("Invalid IP", row[3])
            print("{} will not be backed up" .format(serial))
        if port == "Invalid port":
            print("The port in the csv file is not a number:", row[4])
            print("Cannot connect to {}" .format(serial))
        else:
            home_dir = str(Path.home()) #find user home dir
            backup_dir = home_dir+"/backup/"+company+"/"+serial+"/" #location of saved backup files
            temp_dir = home_dir+"/backup/tmp/" #temp working dir
            valdir = validate_dir(backup_dir) #valdate if dir exist, if not create it
            valdir = validate_dir(temp_dir) #valdate if dir exist, if not create it
            print("Backup file will be saved in: ", backup_dir)
            connection = user+"@"+ip+":fgt-config"
            print('scp -o StrictHostKeyChecking=no -P %s %s %s' % (port, connection, temp_dir))
            #child = pexpect.spawn('scp -o StrictHostKeyChecking=no -P %s %s %s' % (port, connection, temp_dir)) #format old way
            child = pexpect.spawn('scp -o StrictHostKeyChecking=no -P {} {} {}'.format(port, connection, temp_dir)) #format new way
            c = child.expect([pexpect.TIMEOUT, "assword:"], timeout=5) # wait 5 sec for password
            if c == 0:
                print("Error: connection timed out please check if the device is up")
                child.terminate()
            if c == 1:
                child.sendline(upass)
                i = child.expect([pexpect.TIMEOUT, "denied", pexpect.EOF], timeout=20) # wait 20 sec for EOF error or timeout
                if i == 0:
                    print("Error: Connection timed out please check if the device is up")
                    child.terminate()
                if i == 1:
                    print("Error: Access deniedplease check your password")
                    child.terminate()
                if i == 2:
                    src = temp_dir+"fgt-config"
                    fm = move_file(src, backup_dir, serial)
                    print("Device {} backed up to:" .format(serial))
                    print (fm)

            

