#!/usr/bin/env python3
from pwn import *
import socket

# TODO: Fill in the connection details
HOST = "localhost"  # Replace with the actual server IP/DNS
PORT = 1337         # Replace with the actual server port

# Path to your local valid_pass.c file
VALID_PASS_FILE = "src/valid_pass.c"

def main():
    # Connect to the remote service
    log.info(f"Connecting to {HOST}:{PORT}")
    conn = remote(HOST, PORT)

    # Read the local valid_pass.c file
    log.info(f"Reading {VALID_PASS_FILE}")
    try:
        with open(VALID_PASS_FILE, 'rb') as f:
            code = f.read()
    except FileNotFoundError:
        log.error(f"File {VALID_PASS_FILE} not found!")
        log.error("Make sure you have created your valid_pass.c file in the src/ directory")
        conn.close()
        return

    # Send the code to the server
    log.info(f"Sending {len(code)} bytes of code")
    conn.send(code)

    # Send EOF to signal end of input
    conn.shutdown('send')

    # Receive and print all output
    log.info("Receiving output from server...")

    print(conn.recvall().decode("utf-8"))

    conn.close()

if __name__ == "__main__":
    main()
