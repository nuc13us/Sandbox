import subprocess

def stop():
  args = ["VBoxManage", "controlvm", "SandBox","savestate"]
  print "Resuming VM!!!!"
  try:
    subprocess.check_output(args,shell=True)
    sleep(10)
  except Exception as e:
    print "Cannot the save the state of the VM:(:("
