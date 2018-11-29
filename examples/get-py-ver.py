from sys import exit
from platform import python_version


pver = python_version()
pv = int(pver[0])
#if python version is not 2.7 EXIT!
if pv >= 3:
   print("Sorry, this script requires Python 2.x, not Python 3.x")
   exit(1)
else:
   print('Python version is: ', python_version())
