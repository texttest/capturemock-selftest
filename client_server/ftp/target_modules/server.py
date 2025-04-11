import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer()

# Define a new user having full r/w permissions and a read-only
# anonymous user
authorizer.add_user('user', '12345', '.', perm='elradfmwMT')

# Instantiate FTP handler class
handler = FTPHandler
handler.authorizer = authorizer

# Define a customized banner (string returned when client connects)
handler.banner = "pyftpdlib based FTP server ready."

# Specify a masquerade address and the range of ports to use for
# passive connections.  Decomment in case you're behind a NAT.
#handler.masquerade_address = '151.25.42.11'
#handler.passive_ports = range(60000, 65535)

# Instantiate FTP server class and listen on all interfaces, port 2121
address = ('', 0)
server = FTPServer(address, handler)
values = server.socket.getsockname()
address = "localhost:" + str(values[1])
message = "Started FTP server at " + address
print(message, flush=True)

# set a limit for connections
server.max_cons = 256
server.max_cons_per_ip = 5

# start ftp server
server.serve_forever()