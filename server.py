import socket
import threading

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def is_valid_port(port):
    try:
        port = int(port)
        return 0 < port < 65536
    except ValueError:
        return False

def receive_data_from_server(ip, port, update_callback):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        s.connect((ip, port))
        print(f"Connected to {ip}:{port}")

        while True:
            # Receive data from the server
            data = s.recv(4096)  # Increase buffer size if needed
            if not data:
                break  # No more data, exit loop
            decoded_data = data.decode('utf-8')
            print(f"Received data: {decoded_data}")
            update_callback(decoded_data)  # Call the update callback with the new data

    except socket.error as e:
        print(f"Socket error: {e}")
    
    finally:
        # Close the socket connection
        s.close()
        print("Connection closed")

def update_data(data):
    return data

def main():
    # Specify the IP and port of the server
    server_ip = '192.168.1.1'  # Replace with the actual server IP
    server_port = 12345         # Replace with the actual server port

    # Create and start the data receiving thread
    data_thread = threading.Thread(target=receive_data_from_server, args=(server_ip, server_port, update_data))
    data_thread.start()

    # Main thread can continue to perform other tasks
    while True:
        user_input = input("Enter 'quit' to exit: ")
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    main()
