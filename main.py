# by: JOR
# Date: 30APR20
# Function: Takes data from UDP
# Script:

import serial
import socket
import sys
import threading

import Communications.UDPDaemon
import Communications.Utilities
import NMEA.Instrument
import AIS.AIS

myAIS = AIS.AIS.AISReceiver()

print("Main thread started - AIS UDP Listener")
local_host_ip = Communications.Utilities.find_local_ipv4()
# Global variables
write_buffer = ""
ThreadName = 'UDP IPv4 Server'
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Server = Communications.UDPDaemon.UDPServer(1, ThreadName, ServerSocket)

try:
    Server.server_ipv4 = local_host_ip
    Server.setDaemon(True)
    Server.start()
except socket.error as msg:
    sys.stderr.write('Socket error starting UDP server: {}\n'.format(msg) + "\n")
except Exception as error:
    print("Unexpected error starting UDP server:", sys.exc_info()[0])
finally:
    print("UDP Socket open for listening")


while True:
    if len(Server.read_buffer) > 0:
        try:
            print("Received UDP data: " + str(Server.read_buffer) + " from " + Server.client_ipv4 + ":" + str(
                Server.client_port))
            # Read buffer is in bytes, convert to string
            ais_string = "".join(map(chr, Server.read_buffer))
            # Parse the sentence
            myAIS.parse(ais_string)
        except Exception as error:
            print("Unexpected error receiving UDP data:", sys.exc_info()[0])
        finally:
            Server.read_buffer = ""

