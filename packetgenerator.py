from scapy.all import *

def generatepacket (binfile,src,dst,sport,dport):
    print (binfile)
    with open(binfile, 'rb') as f:
        data = f.read()
        
    e=Ether()    
    ip=IP(src=src,dst=dst)
    udp=UDP(sport = int(sport),dport = int(dport))
    payload = data
    packet=e/ip/udp/payload
    sendp(packet)
    
    resultbinfilename = os.path.splitext(os.path.basename(binfile))[0] + '.pcap'
    resultbinfile = os.path.join (os.path.dirname(binfile),resultbinfilename)  
    wrpcap (resultbinfile,packet)
    
if __name__ == "__main__":
   if len(sys.argv) <= 5:
       print "Usage: %s <File Name> <SourceIP> <DestionaIP> <SourcePort> <DestinationPort>" % sys.argv[0]
       sys.exit(1)

   generatepacket(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])