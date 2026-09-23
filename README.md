# Mininet Bootstrap

A hands-on exercise to get started with [Mininet](https://mininet.org) and to study how bandwidth, latency and
packet loss affect the throughput of a simple TCP/UDP application.

## Contents

- `td.ipynb`: the exercise notebook.
- `apps/`: simple throughput measurement tools
  - `tcp-sender.py` / `tcp-receiver.py`: send a given amount of data over TCP and measure the time it takes
  - `udp-sender.py` / `udp-receiver.py`: the same over UDP
