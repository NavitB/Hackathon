Server

from socket import *
from _thread import *
import threading

# constants
buff_len = 1024
MAGIC_COOKIE = 0xfeedbeef
MESSAGE_TYPE = 0x2
DEST_PORT = 13117
# global variables
TEAMS_THREADS_GROUP1 = []  # (team_thread, team_num, team_name, connection_socket)
TEAMS_THREADS_GROUP2 = []
COUNTER_GROUP1 = 0
COUNTER_GROUP2 = 0
SOURCE_IP = get_if_addr('eth1')  # ip development network  # socket.gethostbyname(socket.gethostname())
SOURCE_PORT = 2066
lock = Lock()

def startServer():
    print("Server started, listening on IP address {0}".format(serverIP))
    serverSocketTCP = socket(AF_INET,SOCK_STREAM) #create tcp socket
    serverSocketTCP.bind((SOURCE_IP,SOURCE_PORT))
    # serverSocket.listen(1)
    while True:
        sendOffersThread = Thread(target = sendOfferByUDP, args = [])
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        connectionSocket.send(sentence)
        connectionSocket.close()
        # except:
        #     # try broadcast UDP
        #     serverUDP = socket(AF_INET, SOCK_DGRAM) # UDP
        #     serverUDP.bind((serverIP, serverPort))
        #     while True:
        #         data, addr = serverUDP.recvfrom(1024) # buffer size is 1024 bytes
        #         print("received message: %s" % data)

def sendOffersByUDP():
    serverSocketUDP = socket(AF_INET, SOCK_DGRAM)
    serverSocketUDP.bind('', DEST_PORT)
    offer = struct.pack('LBH', MAGIC_COOKIE, MESSAGE_TYPE, SOURCE_PORT)
    for i in range(10):
        serverSocketUDP.sendto(offer, ('',DEST_PORT))
        time.sleep(1)

