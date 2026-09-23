import socket
import time

localIP = "127.0.0.1"
localPort = 20003
# Must be >= the sender's message length: a datagram larger than the buffer is truncated
bufferSize = 65535

# The sender's s.close() is never seen here: UDP has no connection to close.
# The sender tells us it is done by sending this special message instead.
END_MSG = b"END"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((localIP, localPort))

while True:
  # No accept(): wait for the first datagram to start a new measurement
  data, addr = s.recvfrom(bufferSize)
  if data == END_MSG:
    # Leftover END from the previous transfer (the sender sends it more than once)
    continue
  total_size = len(data)
  start = time.perf_counter()
  while True:
    # Receive message
    data, addr = s.recvfrom(bufferSize)
    if data == END_MSG:
      break
    total_size += len(data)
  end = time.perf_counter()
  elapsed_ms = (end - start) * 1000
  print(f"Received {total_size} bytes in {elapsed_ms:.3f} ms")
  # Calculate and print the throughput in mbps
