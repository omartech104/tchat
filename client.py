import socket
from rich.console import Console

cosnole = Console()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

done = False

while not done:
    client.send(input("> ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
