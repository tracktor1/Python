import os
import ipaddress
import sys
import shutil
from time import gmtime, strftime

###Set the relative file location to the script location
def relative_path(file_name):
    script_path = os.path.abspath(os.path.dirname(__file__))
    joint_path = os.path.join(script_path, file_name)
    return joint_path


###Validate directory and create if not exists
def validate_dir(dir_path):
    directory = os.path.dirname(dir_path)
    if not os.path.exists(directory):
        print("Creating dir: ", directory)
        os.makedirs(directory)
        return "Creating Dir"
    else:
        return "Dir Exist"

###Check if file exists
def validate_file(path_to_file):
    file = os.path.isfile(path_to_file)
    return file

###Validate IP address
def validate_ip(ipaddr):
    try:
        ip = ipaddress.ip_address(ipaddr) #Validate IP address
        return ipaddr
    except ValueError:
        return "Invalid IP"

###Rename the backup file to date + device serial and move it to destanation directory
def move_file(file_src, dst, serial):
    cur_time = strftime("%Y-%m-%d-%H%M")
    file_dst = dst+cur_time+"-"+serial+".conf"
    if not os.path.exists(file_dst):
        shutil.move(file_src, file_dst)
        return file_dst
    else:
        print("File with the same name exist cannot create backup")
        os.remove(file_src)
        return "File Exist"

###Validate cell is not empty and if it's a number
###if cell is empty it will return 22 for ssh port
def validate_cell(cell):
    if cell in (None, ""):
        cell = 22
        return cell
    else:
        try:
            val = int(cell)
            return cell 
        except ValueError:
            return "Invalid port"



        
