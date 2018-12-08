import os
import ipaddress
import sys


###Set the relative file location to the script location
def relative_path(file_name):
    script_path = os.path.abspath(os.path.dirname(__file__))
    joint_path = os.path.join(script_path, file_name)
    return joint_path

###Validate directory and create if not exist
def validate_dir(dir_path):
    directory = os.path.dirname(dir_path)
    if not os.path.exists(directory):
        print("Creating dir: ", directory)
        os.makedirs(directory)
        return "Creating Dir"
    else:
        return "Dir Exist"

###Validate IP address
def validate_ip(ipaddr):
    try:
        ip = ipaddress.ip_address(ipaddr) #Validate IP address
        return ipaddr
    except ValueError:
        return "Invalid IP"



