from vboxapi import VirtualBoxManager
#import TShark
import subprocess
from time import sleep

def copy(FileName):
  args = ["cp",FileName,"/home/nuc13us/VirtualBox\ VMs/SandBoxSharred/"]
  try:
    subprocess.call("cp Lab_01-3.malware /home/nuc13us/VirtualBox\ VMs/SandBoxSharred/" )
  except Exception as e:
    print "Cannot copy the file"


def start():
  mgr = VirtualBoxManager(None, None)
  vbox = mgr.vbox
  name = "SandBox"
  mach = vbox.findMachine(name)
  session = mgr.mgr.getSessionObject(vbox)
  progress = mach.launchVMProcess(session, "gui", "")
  progress.waitForCompletion(-1)
  sleep(120)

def execute(user,passwd,malware):

  print "Executing malware inside the VM"
  try:
    executeProcess(user,passwd,malware)
  except Exception as e:
    print "failed to execute the malware"

def capturePackets():
    print "Capturing network packets"
    args = ["tcpdump"]
    try:
        dump = subprocess.call("tcpdump",shell=True)
        fo = open("networkCapture","w+")
        fo.write(dump)
	sleep(10)
    except Exception as e:
        print "Cannot run tcpdump and open the file"

def DumpRAM():

  args = ["vboxmanage", "debugvm","SandBox", "dumpvmcore", "--filename", "dump.elf"]
  try:
    subprocess.call("vboxmanage debugvm SandBox dumpvmcore --filename dump.elf", shell=True)
    sleep(5)
  except Exception as e:
    print "Cannot Dump the RAM"

def stop():
  args = ["VBoxManage", "controlvm", "SandBox","savestate"]
  try:
     print "Saving the state of the VM!!!!!!!!"
     subprocess.call("VBoxManage controlvm SandBox savestate", shell=True)
     sleep(5)
  except Exception as e:
    print "Cannot save the state of the VM:(:("
