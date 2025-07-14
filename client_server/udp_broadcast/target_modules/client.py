import socket, sys
import time

# Configuration
BROADCAST_IP = '255.255.255.255'
ADDRESS = sys.argv[1]
host, port = ADDRESS.split(":")
MESSAGE = b'discover'

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

sock.settimeout(1)  # timeout for receiving

sock.bind((host, 0))  # Bind to any available local port

# Send broadcast
sock.sendto(MESSAGE, (BROADCAST_IP, int(port)))

# Receive response
try:
    for _ in range(2):
        data, addr = sock.recvfrom(1024)
        print(f"Received response: {data.decode()}")
except ConnectionResetError as e:
    print(f"Connection reset by peer (likely ICMP unreachable): {e}")
except socket.timeout:
    print("No response received.")
finally:
    sock.close()
