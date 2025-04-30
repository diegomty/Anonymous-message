import re
import os
import time
import platform
import base64
from twilio.rest import Client  # Nueva librería

print("[*] Checking Requirements Module")

# Configuración de Twilio (REMPLAZA ESTOS DATOS)
TWILIO_ACCOUNT_SID = "ACbac7cb6ca2e954b84a8967f6da6383ec"      # Encuéntralo en https://console.twilio.com
TWILIO_AUTH_TOKEN = "814e35fbddff18af2728bf64c20625de"        # Token de tu cuenta Twilio
TWILIO_PHONE_NUMBER = "+19787332414"      # Tu número Twilio Mexicano (+52)

if platform.system().startswith("Linux"):
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        from twilio.rest import Client
    except:
        os.system("python3 -m pip install twilio -q -q -q")
        from twilio.rest import Client
elif platform.system().startswith("Windows"):
    try:
        import requests
    except ImportError:
        os.system("python -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        from twilio.rest import Client
    except:
        os.system("python -m pip install twilio -q -q -q")
        from twilio.rest import Client

colorama.deinit()

banner = Center.XCenter(r"""
                _______ _    _  _______     ____  __  __ ______
               / /  ___/ \  | |/ / ____|   / ___||  \/  / ___\ \`
              | || |_ / _ \ | ' /|  _| ____\___ \| |\/| \___ \| |
             < < |  _/ ___ \| . \| |__|_____|__) | |  | |___) |> >
              | ||_|/_/   \_\_|\_\_____|   |____/|_|  |_|____/| |
               \_\                                           /_/
                      SEND MESSAGE ANONYMOUSLY (Twilio MX)
""")

def check_net1():
    print(termcolor.colored("[*] Checking Internet Connection:- ", 'cyan'))
    url = "https://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print(Fore.GREEN+"[*] Connected to the Internet")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        menu()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(Fore.RED+'[*] No Internet Connection....')

def menu():
    ans = True
    while ans:
        print(termcolor.colored("""
      1. Usage
      2. Send SMS
      3. Exit/Quit
      """, 'yellow'))
        ans = input(termcolor.colored("Choose From Given Options: ", 'cyan'))
        if ans == "1":
            print("\033c")
            usage1()
        elif ans == "2":
            print("\033c")
            main_check1()
        elif ans == "3":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            print(Fore.GREEN+"\n [+] Thanks For Using Fake-SMS! See You Tomorrow")
            ans = None
        else:
            print(Fore.RED+"\n [+] Not Valid Choice Try again")

def usage1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    print(termcolor.colored('''
      \n    1. Your Country Code Must Be without +
    2. Country Code Example: 52 for Mexico
    3. Your Phone Number Must be Start Without 0
    4. Full Usage: 5215512345678 (Mexico: 52 + 55-1234-5678)

    ..........NOTE: No Daily Limits (Twilio)...........
      ''', 'magenta'))

def send_sms_twilio(number, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=f'+{number}'
    )
    return message.sid

def main_check1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    x = input(termcolor.colored("\n[*] Enter Your Number (e.g., 5215512345678):- ", 'green'))
    y = input(termcolor.colored("\n[*] Enter Your Message:- ", 'blue'))
    
    print(termcolor.colored("\n[*] Sending message...", 'yellow'))
    time.sleep(2)
    
    try:
        sid = send_sms_twilio(x, y)
        print(termcolor.colored(f'\n[ ✔ ] Message sent! SID: {sid}', 'green'))
    except Exception as e:
        print(termcolor.colored(f'\n[ X ] Error: {str(e)}', 'red'))
        if "Unauthorized" in str(e):
            print(termcolor.colored('  → Check your Twilio SID/Token!', 'red'))

def op():
    try:
        if platform.system().startswith("Windows"):
            os.system("cls")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            check_net1()
        elif platform.system().startswith("Linux"):
            print("\033c")
            check_net1()
        else:
            print(termcolor.colored("Please Use Windows Or Linux OS!", 'red'))
    except KeyboardInterrupt:
        print(termcolor.colored("\n [*]You Pressed The Exit Button!", 'red'))
        quit()

op()