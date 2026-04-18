import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# TTL = 1 → stays in local network
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

message = "Hello Group! This is Group Communication."

sock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))

print("Message sent to group")