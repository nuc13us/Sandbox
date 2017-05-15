import sys
import magic # File Type
import hashlib # md5 of the file
import subprocess #strings command
import requests #virustotal API
from time import sleep

############################[static analysis]####################################

def filetype(FileName,fo):
  """
  m = magic.open(magic.MAGIC_NONE) 
  m.load()
  FileType = m.file(FileName)
  """
  print "Finding the file type!!!!!!!"
  args = ["file",FileName]
  FileType = subprocess.check_output(args)
  fo.write("File type of the malware is: " + "\n" + FileType + "\n")
  sleep(3)

def md5sum(FileName,fo):
  print "Finding the md5 hash of the malware!!!!!!!!!"
  md5hash = hashlib.md5(open(FileName,'rb').read()).hexdigest()
  fo.write("md5sum of the file is:" + md5hash + "\n")
  sleep(3)

def strings(FileName,fo):
  print "Finding the strings of the malware!!!!!!!!!!"
  output = subprocess.check_output(["strings", FileName])
  fo.write("Strings of the binary are:" + "\n" +output + "\n")
  sleep(3)

def virustotal(FileName,fo):
  print "Getting results form virustotal"
  md5hash = hashlib.md5(open(FileName,'rb').read()).hexdigest()
  params = {'apikey': '8f40f27a3e64ec43e9f19e8f8b709b1691436329afb3d554fe52e5a9a8b52f38', 'resource': md5hash}
  headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent" : "gzip,  My Python requests library example client or username"}
  try:
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',params=params, headers=headers)
    json_response = response.json()
    fo.write(str(json_response))
    print "Results found in json_format"
    sleep(5)
  except Exception as e:
    print "No network connection please connect to any network"

def yararules(FileName,fo):
  print "Getting YARA_RULES!!!!!!!!!!"
  args = ["yara", "/home/nuc13us/backup/sandbox/rules-master/Packers_index.yar", FileName]
  output = subprocess.check_output(args)
  fo.write("Rules of yara are: " + "\n" + output)


def static(malware):
  fo = open('static.txt',"w+")

  a = "#"*20 + " Static Analysis " + "#"*20
  fo.write(a + "\n")
  filetype(malware,fo)
  md5sum(malware,fo)
  strings(malware,fo)
  virustotal(malware,fo)
  yararules(malware,fo)
