import subprocess
from time import sleep

############################[memory analysis]####################################

#Volatility is a Framework that is used to perform memory anaylsis
#After the completation of the dynamic analysis in sandbox
#We take snapshot of the VM and perform memory analysis

#This function is used to run the command by using voltality command line tool
def run_cmd(image, cmd):
    pargs = ["vol.py", "-f", image , cmd]
    proc = subprocess.Popen(pargs)
    sleep(15)
    return proc

#To list the processes of a system
def pslist(image):
    print "!!!!!!!!Executing psxview"
    a = run_cmd(image,'pslist')
    return a

#This can find processes that have been hidden or unlinked by a rootkit
def psscan(image):
    print "!!!!!!!Executing psscan"
    return run_cmd(image, 'psscan')

#To view the process listing in tree form
def pstree(image):
    print "!!!!!!!!Executing pstree"
    return run_cmd(image,'pstree')

#To display the open handles in a process like files, registry keys, mutexes, threads
def handles(image):
    print "!!!!!!!!!Executing handles"
    return run_cmd(image,'handles')

#This plugin shows you which process privileges are present and enabled
def privs(image):
    print "!!!!!!!!!!Executing privs"
    return run_cmd(image,'privs')

#To display a process's loaded DLLs, use the dlllist command
def dlllist(image):
    print "!!!!!!!!!!Executing dlllist"
    return run_cmd(image,'dlllist')

#To view the list of kernel drivers loaded on the system
def hivescan(image):
    print "!!!!!!!!!!Executing hivescan"
    return run_cmd(image,'hivescan')

#To view the list of kernel drivers loaded on the system
def kernel_modules(image):
    print "!!!!!!!!!!Executing modules"
    return run_cmd(image,'modules')

#This can pick up previously unloaded drivers and drivers that have been hidden/unlinked by rootkits
def kernel_drivers(image):
    print "!!!!!!!!!!Executing modscan"
    return run_cmd(image, 'modscan')

#To find DRIVER_OBJECTs in physical memory using pool tag scanning
def driverscan(image):
    print "!!!!!!!!!!Executing hivelist"
    return run_cmd(image,'driverscan')

#This plugin finds structures known as COMMAND_HISTORY
def bash_history(image):
    print "!!!!!!!!!!Executing hivelist"
    return run_cmd(image,'cmdscan')

#To find _TCPT_OBJECT structures using pool tag scanning
def connscan(image):
    print "!!!!!!!!!!Executing consscan"
    return run_cmd(image,'connscan')

#To detect listening sockets for any protocol (TCP, UDP, RAW, etc)
def sockets(image):
    print "!!!!!!!!!!Executing sockets"
    return run_cmd(image,'sockets')


def memory(image):

  #image = "/home/nuc13us/backup/sandbox/Sandbox/dump.elf"
  fo = open('memory.txt',"w+")
  a = "#"*20 + " Memory Analysis " + "#"*20
  fo.write(a + "\n")
  a = pslist(image)

  fo.write(str(a))
  fo.write(str(psscan(image)))
  fo.write(str(pstree(image)))
  fo.write(str(handles(image)))
  fo.write(str(privs(image)))
  fo.write(str(dlllist(image)))
  fo.write(str(hivescan(image)))
  fo.write(str(kernel_modules(image)))
  fo.write(str(kernel_drivers(image)))
  fo.write(str(driverscan(image)))
  fo.write(str(bash_history(image)))
  fo.write(str(connscan(image)))
  fo.write(str(sockets(image)))
