import sys
import traceback
import winappdbg
import time
import struct
import ctypes


# Log file which we log info to
logfile = None

class MyEventHandler(winappdbg.EventHandler):
###
# A. Declaring variables
###

  # A.1 used to keep track of allocated executable memory
  allocedmem = {}

  # A.2 used to indicate that we've found the entry point
  entrypt = 0x00000000

  #
  # variables used to find and disassemble unpacking loop
  #

  # A.3 used to indicate that we're single stepping
  tracing = -1

  # A.4 remember the last two eip values
  lasteip = [0x00000000,0x00000000]

  # A.5 lowest eip address we see
  lowesteip = 0xffffffff

  # A.6 highest eip address we see
  highesteip = 0x00000000

  # A.7 list of addresses which we've disassembled
  disasmd = []

  # A.8 keeps track of addresses and instructions
  #     that write to the allocated memory block(s)
  writeaddrs = {}

  #
  # variables used to keep track of created processes
  #
  # A.9 keeps track of created processes to map
  #     hProcess from WriteProcessMemory() back to
  #     process name
  createdprocesses = {}

  # A.10 keeps track of processes that were created
  #      with the CREATE_SUSPENDED flag set
  createsuspended = {}

  #
  # variables used for logging
  #

  # A.11 used to keep a log of events
  eventlog = []
###
# C. API Hooks
###

  ### C.1
  # apiHooks: winappdbg defined hash of API calls to hook
  #
  #     Each entry is indexed by library name and is an array of
  #     tuples consisting of API call name and number of args
  ###

  apiHooks = {
    "kernel32.dll":[
      ("VirtualAlloc",4),
      ("VirtualAllocEx",5),
      ("IsDebuggerPresent",0),
      ("CreateProcessA",10),
      ("CreateProcessW",10),
      ("WriteProcessMemory",5)
    ],
    "advapi32.dll":[
      ("CryptDecrypt",6)
    ],
    "wininet.dll":[
      ("InternetOpenA",5),
      ("InternetOpenW",5)
    ],
    "ntdll.dll":[
      ("RtlDecompressBuffer",6)
    ],
    "secur32.dll":[
      ("EncryptMessage",4),
      ("DecryptMessage",4)
    ]
  }

  def post_VirtualAllocEx(self,event,retval):
    try:
      # C.2.1 Get the return address and arguments

      (ra,(hProcess,lpAddress,dwSize,flAllocationType,flProtect)) = self.get_funcargs(event)

      # Get an instance to the debugger which triggered the event
      # and also the process id and thread id of the process to which
      # the event pertains

      d = event.debug
      pid = event.get_pid()
      tid = event.get_tid()

      # Log the fact that we've seen a VirtualAllocEx() call

      log("[*] <%d:%d> 0x%x: VirtualAllocEx(0x%x,0x%x,0x%x (%d),0x%x,0x%03x) = 0x%x" % (pid,tid,ra,hProcess,lpAddress,dwSize,dwSize,flAllocationType,flProtect,retval))

      # C.2.2 All the memory protection bits which include EXECUTE
      # permission use bits 4 - 7, which is nicely matched
      # by masking (ANDing) it with 0xf0 and checking for a
      # non-zero result

      if (flProtect & 0x0f0):
        log("[-]   Request for EXECUTEable memory")

        # We can only set page guards on our own process
        # otherwise page guard exception will occur in
        # system code when this process attempts to write
        # to the allocated memory.
        # This causes ZwWriteVirtualMemory() to fail

        # We can, however, set a page guard on it when
        # this process creates the remote thread, as it
        # will have presumably stopped writing to the
        # other process' memory at that point.

        # C.2.2.1 Check that this VirtualAllocEx() call is for
        # the current process (hProcess == -1), and if
        # so, ask the winappdbg debugger instance to
        # create a page guard on the memory region.
        # Also add information about the allocated region
        # to our allocedmem hash, indexed by pid and
        # base address.

        if (hProcess == 0xffffffff):
          d.watch_buffer(pid,retval,dwSize - 1,self.guard_page_exemem)
          self.allocedmem[(pid,retval)] = dwSize

      # C.2.3 Create a JSON event log entry

      self.eventlog.append({
        "time": time.time(),
        "name": "VirtualAllocEx",
        "type": "Win32 API",
        "pid": pid,
        "tid": tid,
        "addr": ra,
        "args": {
          "hProcess": hProcess,
          "lpAddress": lpAddress,
          "dwSize": dwSize,
          "flAllocationType": flAllocationType,
          "flProtect": flProtect
        },
        "ret": retval
      })
    except:
      traceback.print_exc()
      raise


  def post_VirtualAlloc(self,event,retval):
    try:
      # C.2.4 Get the return address and arguments

      (ra,(lpAddress,dwSize,flAllocationType,flProtect)) = self.get_funcargs(event)

      # Get an instance to the debugger which triggered the event
      # and also the process id and thread id of the process to which
      # the event pertains

      d = event.debug
      pid = event.get_pid()
      tid = event.get_tid()

      # Log the fact that we've seen a VirtualAlloc() call
      # This is so that we get the address in the debuggee code from which it was called
      # where as if we just let the VirtualAllocEx() hook log it, the address from
      # which it was called is inside the VirtualAlloc() code in kernel32.dll

      log("[*] <%d:%d> 0x%x: VirtualAlloc(0x%x,0x%x (%d),0x%x,0x%03x) = 0x%x" % (pid,tid,ra,lpAddress,dwSize,dwSize,flAllocationType,flProtect,retval))

      # C.2.5 Create a JSON event log entry

      self.eventlog.append({
        "time": time.time(),
        "name": "VirtualAlloc",
        "type": "Win32 API",
        "pid": pid,
        "tid": tid,
        "addr": ra,
        "args": {
          "lpAddress": lpAddress,
          "dwSize": dwSize,
          "flAllocationType": flAllocationType,
          "flProtect": flProtect
        },
        "ret": retval
      })
    except:
      traceback.print_exc()
      raise
