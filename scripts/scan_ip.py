#!/usr/bin/env python3

# Createed by e-seng on GitHub

import os
import subprocess as subp
import sys

def main():
    # usage: ./scan_ip.py <ip> [OPTIOMS]

    if len(sys.argv) == 1:
        display_help()
        return

    ip = sys.argv[1]

    # setting flags
    run_initial = "-i" in sys.argv
    run_deep = "-d" in sys.argv
    run_deepest = "-D" in sys.argv
    run_default = not (run_initial or run_deep)

    overwrite = "-ow" in sys.argv or run_initial or run_deep or run_deepest

    if "-h" in sys.argv:
        display_help()
        return

    print(f"Scanning {ip}...")
    # file names
    folder_name = f"scans-{ip}"
    initial_scan = "initial"
    deep_scan = "deep_scan"
    deepest_scan = "deepest_scan"

    # check for existing folder/files
    if not os.path.exists(folder_name): os.makedirs(folder_name)

    scan_exists = os.path.isfile(f"{folder_name}/{initial_scan}") or os.path.isfile(f"{folder_name}/{deep_scan}")
    if(run_default and not overwrite and scan_exists):
        print(f"Scan already completed for {ip}, use -ow to overwrite if necessary")
        return

    if run_default or run_initial:
        subp.run(f"nmap {ip} -sV -sC -vv -oN {folder_name}/{initial_scan}", shell=True, check=True)
    if run_default or run_deep:
        subp.run(f"nmap {ip} -Pn -A -p- -vv -oN {folder_name}/{deep_scan}", shell=True, check=True)
    if run_deepest:
        subp.run(f"nmap {ip} -sV -sC -Pn -p- -A -vv -oN {folder_name}/{deepest_scan}", shell=True, check=True)

    return


def display_help():
    print("Please specify an ip to scan")
    print("Usage: scan_ip.py <ip> [OPTIONS]")
    print("Ensure ip come directly after 'scan_ip.py'")
    print("OPTIONS:")
    print("\tScans")
    print("\t-----")
    print("\t-i      Initial scan only")
    print("\t-d      Deep scan only")
    print("\t-D      Deepest scan only (will not run by default)")
    print("\t-ow     Overwrite previous scans (Otherwise, will not program if")
    print("\t        previous scan results exist unless at least one of -i, ")
    print("\t        -d or -D is set.)")

    print("\t-h      Displays this help screen")

if __name__ == "__main__": main()
