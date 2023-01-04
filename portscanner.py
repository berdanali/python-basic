import socket
import threading
from queue import Queue



target = "127.0.0.1"
queue=Queue()
open_ports = []
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.connect((target , port ))
        return True
    except:
        return False
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worket():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("port {} is open ".format(port))
            open_ports.append(port)
port_list = range(1,1024)
fill_queue(port_list)

thread_lists = []

for t in range(10):
    thread = threading.Thread(target=worket)
    thread_lists.append(thread)

for thread in thread_lists:
    thread.start()
for thread in thread_lists:
    thread.join()

print("open ports are : ",open_ports)