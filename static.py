import sys
import magic # File Type
import hashlib # md5 of the file
import subprocess #strings command
import requests #virustotal API

############################[static analysis]####################################

def filetype(FileName,fo):
  m = magic.open(magic.MAGIC_NONE)
  m.load()
  FileType = m.file(FileName)
  fo.write("File type of the malware is: " + "\n" + FileType + "\n")

def md5sum(FileName,fo):
  md5hash = hashlib.md5(open(FileName,'rb').read()).hexdigest()
  fo.write("md5sum of the file is:" + md5hash + "\n")

def strings(FileName,fo):
  output = subprocess.check_output(["strings", FileName])
  fo.write("Strings of the binary are:" + "\n" +output + "\n") 

def virustotal(FileName,fo):
  md5hash = hashlib.md5(open(FileName,'rb').read()).hexdigest()
  params = {'apikey': '8f40f27a3e64ec43e9f19e8f8b709b1691436329afb3d554fe52e5a9a8b52f38', 'resource': md5hash}
  headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent" : "gzip,  My Python requests library example client or username"}

  response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',params=params, headers=headers)
  json_response = response.json()

  fo.write(json_response)
 
def static(malware):  
  fo = open('static.txt',"w+")
 
  a = "#"*20 + " Static Analysis " + "#"*20
  fo.write(a + "\n") 
  filetype(malware,fo)
  md5sum(malware,fo)
  strings(malware,fo)
  virustotal(malware,fo)
