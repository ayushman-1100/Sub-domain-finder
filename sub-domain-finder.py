#!/usr/bin/env python3

import socket
import os
from concurrent.futures import ThreadPoolExecutor

# Colors
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[0m"

DEFAULT_WORDLIST = "wordlist.txt"

def banner():
    os.system("clear")
    print(C + """
   ███████╗██╗   ██╗██████╗ ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
   ██╔════╝██║   ██║██╔══██╗██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
   ███████╗██║   ██║██████╔╝█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
   ╚════██║██║   ██║██╔══██╗██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
   ███████║╚██████╔╝██████╔╝██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
""" + W)
    print(Y + "     Fast Subdomain Finder (Wordlist Based)")
    print(G + "     Coded by Ayushman Dubey")
    print(C + "     GitHub: https://github.com/ayushman-1100\n" + W)

def check_subdomain(sub):
    try:
        socket.gethostbyname(sub)
        print(G + "[+] Found:", sub + W)
    except:
        pass

def main():
    banner()
    domain = input(Y + "[?] Enter target domain (example.com): " + W).strip()

    wordlist = input(Y + "[?] Wordlist path (press Enter for default): " + W).strip()
    if wordlist == "":
        wordlist = DEFAULT_WORDLIST

    try:
        with open(wordlist, "r") as f:
            words = f.read().splitlines()
    except:
        print(R + "[!] Wordlist not found!" + W)
        return

    print(Y + f"\n[*] Total words loaded: {len(words)}")
    print(Y + "[*] Scanning started...\n" + W)

    with ThreadPoolExecutor(max_workers=50) as executor:
        for word in words:
            sub = f"{word}.{domain}"
            executor.submit(check_subdomain, sub)

if __name__ == "__main__":
    main()
