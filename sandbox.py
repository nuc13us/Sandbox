import sys
import magic # File Type
import hashlib # md5 of the file
import subprocess #strings command

def filetype(FileName):
  m = magic.open(magic.MAGIC_NONE)
  m.load()
  FileType = m.file(FileName)
  print "File type of the malware is:"
  print FileType + "\n"

def md5sum(FileName):
  md5hash = hashlib.md5(open(FileName,'rb').read()).hexdigest()
  print "md5sum of the file is:"
  print md5hash + "\n"

def strings(FileName):
  output = subprocess.check_output(["strings", FileName])
  print "Strings of the binary are:"
  print output
  output = output.replace("\n",",").strip()
    
  
if __name__ == "__main__":

  if len(sys.argv) == 1:
    print "Enter your file name as argument"
    sys.exit()
  print "#"*20 + " Static Analysis " + "#"*20
  
  filetype(sys.argv[1])
  md5sum(sys.argv[1])
  strings(sys.argv[1])



