import socket
import threading
from rich.console import Console
from datetime import datetime

console = Console()

nickname = input("Choose your name for the chat : ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5500))


def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NAME":
                client.send(nickname.encode("ascii"))
            else:
                timestamp = datetime.now().strftime("%H:%M:%S")
                # Style messages depending on content
                if "joined the chat" in message.lower():
                    console.print(f"[{timestamp}] {message}", style="bold green")
                elif "left the chat" in message.lower():
                    console.print(f"[{timestamp}] {message}", style="bold red")
                else:
                    console.print(f"[{timestamp}] {message}", style="bold cyan")
        except:
            console.print("[bold red]An error occurred![/]")
            client.close()
            break


def write():
    while True:
        msg_content = input("")
        message = f"[bold yellow]{nickname}[/]: {msg_content}"
        client.send(message.encode("ascii"))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

