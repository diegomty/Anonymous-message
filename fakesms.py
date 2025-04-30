#!/usr/bin/env python3
import smtplib
import random
import time
from email.message import EmailMessage
import socks  # Opcional: Para usar con TOR
import socket
import os
import platform
from pystyle import *
from colorama import Fore, Back, Style
import termcolor
import colorama

# ===== CONFIGURACIÓN ===== #
# Proxy SOCKS5 (TOR) - Descomenta para usar
# socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
# socket.socket = socks.socksocket

# Gateways SMS por operadora (México)
GATEWAYS = {
    "Telcel": "@sms.telcel.com",
    "AT&T": "@txt.att.net",
    "Movistar": "@movistar.com"
}

# Servidores SMTP públicos (rotación aleatoria)
SMTP_SERVERS = [
    ("smtp.gmail.com", 587),
    ("smtp-mail.outlook.com", 587),
    ("mail.yahoo.com", 587),
    ("smtp.protonmail.com", 587)
]

# ===== FUNCIONES PRINCIPALES ===== #
def send_anonymous_sms(number, message):
    """Envía un SMS anónimo via SMTP."""
    try:
        smtp_server, port = random.choice(SMTP_SERVERS)
        fake_email = f"anon{random.randint(1000,9999)}@tmpmail.org"
        gateway = GATEWAYS["AT&T"]  # Cambia según operadora destino
        
        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = ""
        msg["From"] = fake_email
        msg["To"] = f"{number}{gateway}"
        
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(Fore.RED + f"[X] Error: {str(e)}")
        return False

# ===== INTERFAZ Y MENÚ ===== #
colorama.init()
banner = Center.XCenter(r"""
                _______ _    _  _______     ____  __  __ ______
               / /  ___/ \  | |/ / ____|   / ___||  \/  / ___\ \`
              | || |_ / _ \ | ' /|  _| ____\___ \| |\/| \___ \| |
             < < |  _/ ___ \| . \| |__|_____|__) | |  | |___) |> >
              | ||_|/_/   \_\_|\_\_____|   |____/|_|  |_|____/| |
               \_\                                           /_/
                      SEND MESSAGE ANONYMOUSLY (SMTP MODE)
""")

def check_internet():
    """Verifica conexión a Internet."""
    print(termcolor.colored("[*] Checking Internet Connection...", 'cyan'))
    try:
        requests.get("https://www.google.com", timeout=5)
        print(Fore.GREEN + "[*] Connected!")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        menu()
    except:
        print(Fore.RED + "[X] No Internet Connection!")

def menu():
    """Menú principal."""
    while True:
        print(termcolor.colored("""
      1. Usage Instructions
      2. Send SMS
      3. Exit
      """, 'yellow'))
        choice = input(termcolor.colored("Choose an option: ", 'cyan'))
        
        if choice == "1":
            show_usage()
        elif choice == "2":
            send_sms_menu()
        elif choice == "3":
            print(Fore.GREEN + "\n[+] Thanks for using Fake-SMS!")
            break
        else:
            print(Fore.RED + "\n[!] Invalid option!")

def show_usage():
    """Muestra instrucciones de uso."""
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    print(termcolor.colored('''
    1. Country Code MUST start without +
    2. Example for Mexico: 5215512345678
    3. Only 1 SMS per 24h (server limits)
    ''', 'magenta'))

def send_sms_menu():
    """Interfaz para enviar SMS."""
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    number = input(termcolor.colored("\n[*] Enter Number (e.g., 5215512345678): ", 'green'))
    message = input(termcolor.colored("\n[*] Enter Message: ", 'blue'))
    
    print(termcolor.colored("\n[*] Sending via SMTP...", 'yellow'))
    if send_anonymous_sms(number, message):
        print(Fore.GREEN + f"\n[✔] Sent to {number}!")
    else:
        print(Fore.RED + "\n[X] Failed. Try again later.")

# ===== EJECUCIÓN ===== #
if __name__ == "__main__":
    try:
        if platform.system() in ["Linux", "Windows"]:
            check_internet()
        else:
            print(Fore.RED + "[!] Use Linux/Windows only!")
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Stopped by user.")