import socket
import os

## http://docs.cs.up.ac.za/programming/python/python-2.7.9-docs-html/library/socket.html
## http://www.pythonforpentesting.com/2014/03/python-raw-sockets.html
## http://bt3gl.github.io/building-a-udp-scanner-with-pythons-socket-module.html
## http://stackoverflow.com/questions/462439/packet-sniffing-in-python-windows
## http://www.binarytides.com/python-packet-sniffer-code-linux/
## http://www.binarytides.com/python-socket-server-code-example/
## http://www.binarytides.com/python-socket-programming-tutorial/
## http://www.binarytides.com/python-syn-flood-program-raw-sockets-linux/
## http://www.binarytides.com/raw-socket-programming-in-python-linux/
## http://pylibpcap.sourceforge.net/

# host to listen
HOST = '10.199.24.36'

def sniffing(host, win, socket_prot):
    while 1:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_prot)
        sniffer.bind((host, 0))

        # include the IP headers in the captured packets
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if win == 1:
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        # read in a single packet
        print sniffer.recvfrom(65565)

def main(host):
    print os.name
    if os.name == 'nt':
        sniffing(host, 1, socket.IPPROTO_IP)
    else:
        sniffing(host, 0, socket.IPPROTO_ICMP)

if __name__ == '__main__':
    main(HOST)
