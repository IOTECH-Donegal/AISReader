import socket

def find_local_ipv4():
    local_host_ip = str(socket.gethostbyname(socket.gethostname()))
    if local_host_ip == '127.0.0.1':
        print("You must set the hostname correctly in /etc/hosts!")
        print("Existing until you sort this!!")
        exit(0)
    return local_host_ip
