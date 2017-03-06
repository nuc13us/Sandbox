from vboxapi import VirtualBoxManager

def copy(FileName):
  args = ["cp",FileName,"VirtualBox\ VMs/SandBoxSharred/"]
  try:
    subprocess.check_output(args)
  execpt Exception,e:
    print "Cannot copy the file"


def start():
  mgr = VirtualBoxManager(None, None)
  vbox = mgr.vbox
  name = "SandBox"
  mach = vbox.findMachine(name)
  session = mgr.mgr.getSessionObject(vbox)
  progress = mach.launchVMProcess(session, "gui", "")
  progress.waitForCompletion(-1)


