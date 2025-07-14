import socket, time, os

LISTEN_IP = '127.0.0.1'  # Listen on all interfaces
PORT = 0

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((LISTEN_IP, PORT))
host, port = sock.getsockname()
address = host + ":" + str(port)
print(f"Listening for broadcasts on {address}", flush=True)

while True:
    data, addr = sock.recvfrom(1024)
    with open("serverout.cpmock", "w") as f:
        print(f"Received from {addr}: {data.decode()}", file=f)

    response = b'ACK'
    sock.sendto(response, addr)
    time.sleep(0.1)
