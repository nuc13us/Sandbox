import subprocess

args = ["yara", "/home/nuc13us/backup/sandbox/rules-master/Packers_index.yar", "Lab_01-3.malware"]
output = subprocess.check_output(args)
print output
