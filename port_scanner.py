import socket

def port_scanner(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")
