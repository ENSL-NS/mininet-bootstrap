import socket
import time

localIP = "127.0.0.1"
localPort = 20003
bufferSize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Allow restarting the server right away without "Address already in use"
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((localIP, localPort))
s.listen(1) 

while True:
  conn, addr = s.accept()
  total_size = 0
  start = time.perf_counter()
  while True:
    # Receive message
    data = conn.recv(bufferSize)
    if not data:
      break
    total_size += len(data)
  conn.close()
  end = time.perf_counter()
  elapsed_ms = (end - start) * 1000
  print(f"{elapsed_ms:.3f} ms")
  # Calculate and print the throughput in mbps
