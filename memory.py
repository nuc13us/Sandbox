import subprocess

############################[memory analysis]####################################

def run_cmd(image, cmd):
    pargs = ["vol.py", "-f", image ,"--profile="+imagetype, cmd]
    proc = subprocess.Popen(pargs, stdout=subprocess.PIPE)
    return proc

def psxview(image):
    return run_cmd(image,'psxview')

def pslist(image):
    return  run_cmd(image,'pslist')

def pstree(image):
    return run_cmd(image,'pstree')

def threads(image):
    return run_cmd(image,'threads')

def netstat(image):
    return run_cmd(image,'netstat')

def ipconfig(image):
    return run_cmd(image,'ipconfig')

def library_list(image):
    return run_cmd(image,'library_list')

def check_modules(image):
    return run_cmd(image,'check_modules')

def hidden_modules(image):
    return run_cmd(image,'hidden_modules')

def kernel_opened_files(image):
    return run_cmd(image,'kernel_opened_files')

def keyboard_notifiers(image):
    return run_cmd(image,'keyboard_notifiers')

def check_syscall(image):
    return run_cmd(image,'check_syscall')

def bash_history(image):
    return run_cmd(image,'bash')

def netfilter(image):
    return run_cmd(image,'netfilter')

def plthook(image):
    return run_cmd(image,'plthook')

def apihooks(image):
    return run_cmd(image,'apihooks')

def memory(image):
  
  fo = open('memory.txt',"w+")
  a = "#"*20 + " Memory Analysis " + "#"*20
  fo.write(a + "\n")

  fo.write(psxview(image))
  fo.write(pslist(image))
  fo.write(pstree(image))
  fo.write(threads(image))
  fo.write(netstat(image))
  fo.write(ipconfig(image))
  fo.write(library_list(image))
  fo.write(check_modules(image))
  fo.write(hidden_modules(image))
  fo.write(kernel_opened_files(image))
  fo.write(keyboard_notifiers(image))
  fo.write(check_syscall(image))
  fo.write(bash_history(image))
  fo.write(netfilter(image))
  fo.write(plthook(image))
  fo.write(apihooks(image))

