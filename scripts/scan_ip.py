#!/usr/bin/env python3

# Createed by e-seng on GitHub

import os
import subprocess as subp
import sys

def main():
    # usage: ./scan_ip.py <ip> [OPTIOMS]
    # note: there are no options currently :/

    if len(sys.argv) == 1:
        print("Please specify an ip to scan")
        print("Usage: scan_ip.py <ip>")
        return

    ip = sys.argv[1]

    print(f"Scanning {ip}...")
    # file names
    folder_name = "scans"
    initial_scan = "initial"
    deep_scan = "deep_scan"
    deepest_scan = "deepest_scan"

    if not os.path.exists(folder_name): os.makedirs(folder_name)

    subp.run(f"nmap {ip} -sV -sC -oN {folder_name}/{initial_scan}", shell=True, check=True)
    subp.run(f"nmap {ip} -Pn -A -p- -oN {folder_name}/{deep_scan}", shell=True, check=True)
    subp.run(f"nmap {ip} -sV -sC -Pn -p- -A -oN {folder_name}/{deepest_scan}", shell=True, check=True)

    return


if __name__ == "__main__": main()
