import socket

# Port Scanner Function
def port_scanner(target, ports):
    open_ports = []
    for port in ports:
        try:
            # Try to connect to the target
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    
    return open_ports
