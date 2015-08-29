from scapy.all import *
from scapy.utils import rdpcap

def generatepacket (binfile):

    pkts=rdpcap(binfile)  # could be used like this rdpcap("filename",500) fetches first 500 pkts
    for pkt in pkts:
         sendp(pkt) #sending packet at layer 2

if __name__ == "__main__":
   if len(sys.argv) <= 1:
       print "Usage: %s <File Name> " % sys.argv[0]
       sys.exit(1)

   generatepacket(sys.argv[1])