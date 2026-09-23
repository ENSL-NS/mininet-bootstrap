import socket
import time

serverIP = "127.0.0.1"
serverPort = 20003

total_bytes = 1000000 # what amount for a good estimate?
msg_len = 1024 # what size to maximize throughput? (max 65507 for UDP)

message = b"x" * msg_len

# Note that UDP has no connection: no connect/accept, and no close the receiver can see.
# We therefore send a special END message to tell the receiver we are done.
END_MSG = b"END"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sent = 0
start = time.perf_counter()
while sent < total_bytes:
  chunk = message[:min(msg_len, total_bytes - sent)]
  s.sendto(chunk, (serverIP, serverPort))
  sent += len(chunk)
# Signal the end of the transfer.
s.sendto(END_MSG, (serverIP, serverPort))
s.close()
end = time.perf_counter()
elapsed_ms = (end - start) * 1000
print(f"Sent {sent} bytes in {elapsed_ms:.3f} ms")
