import socket
import threading
from datetime import datetime
from logger import HoneypotLogger
from report import generate_report

HOST = "0.0.0.0"
PORT = 2222

logger = HoneypotLogger()
running = True
server_socket = None


def handle_client(conn, addr):
    ip = addr[0]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logger.log_connection(ip, timestamp)

    print("\n[+] Connection attempt detected")
    print("IP:", ip)
    print("Timestamp:", timestamp)

    try:
        conn.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n")
        conn.send(b"login: ")

        username = conn.recv(1024).decode().strip()

        conn.send(b"password: ")
        password = conn.recv(1024).decode().strip()

        logger.log_credentials(ip, username, password)

        print("\n[+] Credential attempt captured")
        print("Username:", username)
        print("Password:", password)

        conn.send(b"Permission denied\n")

    except:
        pass

    finally:
        conn.close()


def start_server():
    global server_socket, running

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Honeypot running on port {PORT} (SSH simulation)")
    print("Press CTRL+C or type 'exit' to stop\n")

    while running:
        try:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
        except:
            break


def command_listener():
    global running, server_socket

    while running:
        cmd = input().strip().lower()

        if cmd == "exit":
            print("\nStopping honeypot...")
            running = False

            if server_socket:
                server_socket.close()

            break


def main():
    global running, server_socket

    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    try:
        command_listener()

    except KeyboardInterrupt:
        print("\nStopping honeypot...")
        running = False
        if server_socket:
            server_socket.close()

    server_thread.join()

    print("\nGenerating report...\n")
    generate_report(logger)


if __name__ == "__main__":
    main()