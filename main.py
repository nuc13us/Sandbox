import static
import sys
import memory

if __name__ == "__main__":
  if len(sys.argv) == 1:
    print "Enter your file name as argument"
  sys.exit()
 
  static.static(sys.argv[1])
  memory.memory(sys.argv[2])
    
