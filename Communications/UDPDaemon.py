import socket
from socket import *
import sys
import threading

"""
    UDP for IPv4
    By: JOR
    v0.1    13APR14     Initial tests
    v0.2    17APR14     Added error checking
    v0.3    26APR14     Rewrite threading
    v0.4    16JUL18     Rewrite for Python 3.x
    v0.5    12AUG18     Added binary support
"""


class UDPServer(threading.Thread):
    def __init__(self, thread_id, name, udp_socket):
        threading.Thread.__init__(self)
        self.socket = udp_socket
        self.name = name
        self.thread_id = thread_id
        self.server_ipv4 = ""
        self.server_port = 2001
        self.client_ipv4 = ""
        self.client_port = 2000
        self.read_buffer = []
        self.write_buffer = []

    def run(self):
        print("Starting thread " + str(self.thread_id) + " - " + self.name)
        # Bind the socket
        try:
            self.socket.bind((self.server_ipv4, self.server_port))
        except socket.error as msg:
            sys.stderr.write('Bind failure warning: {}\n'.format(msg))
        except Exception as error:
            print("Bind unexpected error:", sys.exc_info()[0])
        finally:
            print(self.socket)

        # Loop to wait for data
        try:
            while 1:
                data, address = self.socket.recvfrom(1024)
                # record the source of the packet
                self.client_ipv4, self.client_port = address
                # read the data
                self.read_buffer = data
        except socket.error as msg:
            sys.stderr.write('UDP socket warning: {}\n'.format(msg) + "\n")
        except Exception as error:
            print("UDP socket unexpected error:", sys.exc_info()[0])

    def write_udp(self, destination_ipv4, destination_port):
        try:
            bytes_to_send = self.write_buffer
            self.socket.sendto(bytes_to_send, (destination_ipv4, destination_port))
        except socket.error as msg:
            sys.stderr.write('UDP Client: {}\n'.format(msg))

