import socket
import requests
import socks
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
from tqdm import tqdm

init(autoreset=True)

def display_banner():
    print(Fore.YELLOW + """
  RRRR    AAAAA  JJJJJ  SSSSS  EEEEE  CCCCC  
  R   R  A     A    J   S      E      C       
  RRRR   AAAAAAA    J   SSSSS  EEEE   C       
  R  R   A     A    J       S  E      C       
  R   R  A     A  JJJJJ  SSSSS  EEEEE  CCCCC 
                                                                            
 Fast Proxy Checker and Validator by RajExploit404
    """)

def check_proxy(proxy, progress_bar, proxy_type):
    ip, port = proxy.split(':')
    
    try:
        if proxy_type == "http":
            response = requests.get('http://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=5)
            if response.status_code == 200:
                with open('http_active.txt', 'a') as output_file:
                    output_file.write(f"{proxy}\n")
                progress_bar.set_postfix({"Checking": proxy})
                progress_bar.update(1)
                return f"{Fore.GREEN}HTTP Proxy {proxy} is active."
            else:
                progress_bar.set_postfix({"Checking": proxy})
                progress_bar.update(1)
                return f"{Fore.RED}HTTP Proxy {proxy} is not active. Status code: {response.status_code}"

        elif proxy_type == "socks4" or proxy_type == "socks5":
            socks_version = socks.SOCKS4 if proxy_type == "socks4" else socks.SOCKS5
            socks.set_default_proxy(socks_version, ip, int(port))
            socket.socket = socks.socksocket  
            response = requests.get('http://httpbin.org/ip', timeout=5)
            if response.status_code == 200:
                output_file_name = f"{proxy_type}_active.txt"
                with open(output_file_name, 'a') as output_file:
                    output_file.write(f"{proxy}\n")
                progress_bar.set_postfix({"Checking": proxy})
                progress_bar.update(1)
                return f"{Fore.GREEN}{proxy_type.upper()} Proxy {proxy} is active."
            else:
                progress_bar.set_postfix({"Checking": proxy})
                progress_bar.update(1)
                return f"{Fore.RED}{proxy_type.upper()} Proxy {proxy} is not active. Status code: {response.status_code}"

    except (socket.timeout, socket.error, requests.exceptions.RequestException) as e:
        progress_bar.set_postfix({"Checking": proxy})
        progress_bar.update(1)
        return f"{Fore.RED}Proxy {proxy} is not active. Error: {e}"

def read_proxies_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def process_proxies_in_parallel(proxy_list, proxy_type):
    with ThreadPoolExecutor(max_workers=100) as executor:
        with tqdm(total=len(proxy_list), desc=f"Checking {proxy_type.upper()} Proxies", dynamic_ncols=True) as progress_bar:
            results = list(executor.map(lambda proxy: check_proxy(proxy, progress_bar, proxy_type), proxy_list))

    for result in results:
        print(result)

def proxy_menu():
    print(Fore.YELLOW + """
    Select Proxy Type to Check:
    [1] HTTP
    [2] SOCKS4
    [3] SOCKS5
    [4] Exit
    """)

    choice = input(Fore.CYAN + "Enter your choice (1/2/3): ").strip()

    if choice == "1":
        return "http"
    elif choice == "2":
        return "socks4"
    elif choice == "3":
        return "socks5"
    elif choice == "4":
        exit()
    else:
        print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")
        return proxy_menu()

def main():
    display_banner()
    
    proxy_type = proxy_menu()
    
    file_path = input(Fore.CYAN + "Enter the file path (e.g., list.txt): ").strip()
    
    try:
        proxies = read_proxies_from_file(file_path)
    except FileNotFoundError:
        print(Fore.RED + f"File not found: {file_path}. Please check the file path and try again.")
        return

    process_proxies_in_parallel(proxies, proxy_type)

if __name__ == "__main__":
    main()
