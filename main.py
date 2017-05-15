#!/usr/bin/env python

import sys
import static
import dynamic
import memory

if __name__ == "__main__":
  if len(sys.argv) == 1:
    print "Enter your file name as argument"
    sys.exit()

  print "Performing static analysis"
  static.static(sys.argv[1])
  dynamic.dynamic(sys.argv[1],sys.argv[2])
  memory.memory(sys.argv[3])
