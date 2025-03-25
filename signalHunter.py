#!/usr/bin/env python3

import subprocess
import re
import argparse
import shutil


def banner():
    banner_name = r"""

                                  )                              
                           (   ( /(                  )           
    (   (  (            )  )\  )\())   (          ( /(   (   (   
 (  )\  )\))(  (     ( /( ((_)((_)\   ))\   (     )\()) ))\  )(  
 )\((_)((_))\  )\ )  )(_)) _   _((_) /((_)  )\ ) (_))/ /((_)(()\ 
((_)(_) (()(_)_(_/( ((_)_ | | | || |(_))(  _(_/( | |_ (_))   ((_)
(_-<| |/ _` || ' \))/ _` || | | __ || || || ' \))|  _|/ -_) | '_|
/__/|_|\__, ||_||_| \__,_||_| |_||_| \_,_||_||_|  \__|\___| |_|  
       |___/                                                     
"""
    #print(banner_name)
    terminal_width = shutil.get_terminal_size().columns
    centered_banner = "\n".join(line.center(terminal_width) for line in banner_name.split("\n"))
    print(centered_banner)


banner()

print("""
[+] Author   : N3xtGenH4cker
[+] Tool     : WiFi Signal Scanner
[+] Version  : 1.0
[+] GitHub   : https://github.com/N3xtGenH4cker
[+] Disclaimer: This tool is for educational and ethical use only.
                Unauthorized use may violate local laws. Danko!!
""")

def scan_wifi(interface):
    try:
        result = subprocess.check_output(["sudo", "iwlist", interface, "scan"], text=True)
        networks = re.findall(r"Cell \d+ - Address: ([\w:]+).*?Channel:(\d+)", result, re.DOTALL)

        if networks:
            print(f"{'BSSID':<20} {'Channel':<10}")
            print("=" * 30)
            for bssid, channel in networks:
                print(f"{bssid:<20} {channel:<10}")
        else:
            print("No WiFi networks found.")

    except subprocess.CalledProcessError:
        print(f"Error: Unable to scan on interface {interface}. Ensure you have sudo privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan for nearby WiFi networks and display BSSID and channel.")
    parser.add_argument("-i", "--interface", required=True, help="Wireless interface to scan (e.g., wlan0, wlp2s0)")
    
    args = parser.parse_args()
    scan_wifi(args.interface)
