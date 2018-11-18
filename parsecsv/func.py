import os.path
import ipaddress

# set the relative file location to the script location
def relative_path(file_name):
    script_path = os.path.abspath(os.path.dirname(__file__))
    joint_path = os.path.join(script_path, file_name)
    return joint_path

#Validate IP address
def validate_ip(ipaddr):
    try:
        ip = ipaddress.ip_address(unicode(ipaddr)) #Validate IP address
        #print('%s is a correct IP%s address.' % (ip, ip.version))
        return ipaddr
    except ValueError:
        #print('address/netmask is invalid: %s' % ipaddr)
        return "ip not valid"
        #raise Exception("Error")
