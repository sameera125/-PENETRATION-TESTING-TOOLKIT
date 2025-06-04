from port_scanner import port_scanner
from brute_forcer import brute_force_login

print("Penetration Testing Toolkit")
print("1. Port Scanner")
print("2. Brute Forcer")

choice = input("Choose module (1/2): ")

if choice == "1":
    target = input("Enter target domain or IP: ")
    ports = list(map(int, input("Enter ports to scan (comma-separated): ").split(",")))
    port_scanner(target, ports)

elif choice == "2":
    url = input("Enter login URL: ")
    username = input("Enter username: ")
    wordlist_path = input("Enter path to wordlist: ")
    brute_force_login(url, username, wordlist_path)

else:
    print("Invalid choice.")
