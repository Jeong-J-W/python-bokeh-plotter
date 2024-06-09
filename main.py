import server
import agv_message_parser
import bokeh_plotter

def get_ip_from_user():
    ip = input("Enter an IP address: ")
    port = input("Enter a port number: ")

    while True:
        if server.is_valid_ip(ip) and server.is_valid_port(port):
            print("IP address and port are valid.")
            server.receive_data_from_server(ip,port)
            break
        else:
            print("Invalid IP address or port number.")
    
def main():
    get_ip_from_user()
    
    while True:
        server.update_data()
        
        
    

if __name__ == "__main__":
    main()
