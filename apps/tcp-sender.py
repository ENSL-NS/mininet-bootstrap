import socket
import sys
import time

serverIP = "127.0.0.1"
serverPort = 20003

total_bytes = 1000000 # what amount for a good estimate?
msg_len = 1024 # what size to maximize throughput? 

message = b"x" * msg_len

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverIP, serverPort))

sent = 0
start = time.perf_counter()
while sent < total_bytes:
  # Last message may be shorter than msg_len
  chunk = message[:min(msg_len, total_bytes - sent)]
  s.sendall(chunk)
  sent += len(chunk)
s.close()
end = time.perf_counter()
elapsed_ms = (end - start) * 1000
print(f"Sent {sent} bytes in {elapsed_ms:.3f} ms")
