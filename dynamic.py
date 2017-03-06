import subprocess

def check():
  try:
    from vboxapi import VirtualBoxManager
  except ImportError:
    perror('You need to install VirtualBox!')
    return False

def copy(FileName):

    dynamicUtils.copy(FileName)
    print "Copied malware to shared memory!!"

def start():

    
 
 
