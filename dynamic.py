import subprocess
from time import sleep
import dynamicUtils
import stopVM

def check():
  try:
    from vboxapi import VirtualBoxManager
  except Importerror as e:
    print "You need to install VirtualBox!!!"
    return False

def copy(FileName):

  print "Coping file to the shared memory"
  dynamicUtils.copy(FileName)

def start():
  dynamicUtils.start()
  print "Starting the VM!!!!"

def capturePackets():
  print "Capturing network packets!!"
  dynamicUtils.capturePackets()

def run_malware(FileName):
    dynamicUtils.execute('nuc13us', '    ',FileName)

def DumpRAM():
  print "Dumping RAM of the VM!!!!!"
  dynamicUtils.DumpRAM()

def stop():
  dynamicUtils.stop()
 # stopVM.stop()
  print "Resumed the VM!!!"

def dynamic(FileName,time):

  copy(FileName)
  start()
  capturePackets()
  run_malware(FileName)
  DumpRAM()
  stop()
