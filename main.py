#!/usr/bin/env python3

import subprocess
import argparse
import re
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def get_args():
    parser = argparse.ArgumentParser(description="Change MAC address of a network interface.")
    parser.add_argument("-i", "--interface", dest="interface", required=True,
                        help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True,
                        help="New MAC address")
    args = parser.parse_args()
    return args

def is_valid_mac(mac):
    return re.match(r"([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$", mac) is not None

def change_mac(interface, new_mac):
    logging.info(f"Changing MAC address for {interface} to {new_mac}")
    try:
        subprocess.run(["ifconfig", interface, "down"], check=True)
        subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], check=True)
        subprocess.run(["ifconfig", interface, "up"], check=True)
        logging.info(f"MAC address for {interface} successfully changed to {new_mac}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to change MAC address: {e}")
        sys.exit(1)

def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.STDOUT).decode('utf-8')
        mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            logging.error("Could not read MAC address")
            return None
    except subprocess.CalledProcessError as e:
        logging.error(f"Could not execute ifconfig on interface {interface}: {e.output.decode('utf-8').strip()}")
        return None

if __name__ == "__main__":
    options = get_args()

    if not is_valid_mac(options.new_mac):
        logging.error("Invalid MAC address format. Please enter a valid MAC address.")
        sys.exit(1)
    
    current_mac = get_current_mac(options.interface)
    if current_mac:
        logging.info(f"Current MAC: {current_mac}")
        
        change_mac(options.interface, options.new_mac)
        
        updated_mac = get_current_mac(options.interface)
        if updated_mac == options.new_mac:
            logging.info(f"MAC address was successfully changed to {updated_mac}")
        else:
            logging.error("MAC address did not get changed.")
    else:
        logging.error(f"Could not retrieve current MAC address for {options.interface}. Exiting.")
        sys.exit(1)
