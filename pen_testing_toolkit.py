import sys
from port_scanner import port_scanner
from brute_forcer import brute_force

def main():
    print("Penetration Testing Toolkit")
    print("===========================")
    
    # Menu for user to select tools
    print("1. Port Scanner")
    print("2. Brute Forcer")
    print("Enter choice (1 or 2): ")
    choice = input()
    
    if choice == '1':
        # Port Scanner
        target_ip = input("Enter target IP address to scan: ")
        ports_to_scan = [21, 22, 80, 443, 8080]  # Common ports
        open_ports = port_scanner(target_ip, ports_to_scan)
        if open_ports:
            print(f"Open Ports on {target_ip}: {open_ports}")
        else:
            print(f"No open ports found on {target_ip}")
    
    elif choice == '2':
        # Brute Forcer
        login_url = input("Enter the login URL: ")
        usernames_list = ['admin', 'user', 'test']
        passwords_list = ['password123', '1234', 'admin']
        brute_force(login_url, usernames_list, passwords_list)
    
    else:
        print("Invalid choice! Please select either 1 or 2.")
        sys.exit()

if __name__ == "__main__":
    main()
