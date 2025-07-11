#!/usr/bin/env python

import sys, os
from ftplib import FTP, error_perm

servAddr = sys.argv[1]
host, port = servAddr.split(":")

ftp = FTP()
ftp.connect(host, int(port))
try:
    ftp.login("user", "12345")                     # user anonymous, passwd anonymous@

    ftp.retrlines('LIST')           # list directory contents

    ftp.retrlines('RETR README.txt')
    ftp.retrlines('RETR /subdir/absfile.txt')

    try:
        ftp.retrlines('RETR no_such_file')
    except error_perm as e:
        print("Failed to retrieve file", str(e))
finally:
    ftp.quit()
