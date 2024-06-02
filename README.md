This project provides a Python-based script to change the MAC (Media Access Control) address of a network interface on your system. A MAC address is a unique identifier assigned to network interfaces for communications on the physical network segment. Changing your MAC address can be useful for various purposes such as enhancing privacy, bypassing network restrictions, or testing network configurations.
Features

    Change MAC Address: The script allows you to specify a network interface and a new MAC address to change the current MAC address of the network interface.
    Validate MAC Address: It includes validation to ensure the new MAC address is in the correct format.
    Logging: The script uses logging to provide detailed information about the process, including success and error messages.
    Error Handling: It includes error handling to manage issues such as invalid interfaces or MAC addresses.

How It Works

    Disable Network Interface: The script first disables the specified network interface to safely change its MAC address.
    Change MAC Address: It uses system commands to change the MAC address of the network interface to the new specified MAC address.
    Enable Network Interface: After changing the MAC address, the script re-enables the network interface.
    Verification: The script verifies if the MAC address has been successfully changed and logs the result.

Prerequisites

    Python 3.x
    ifconfig command available (usually part of the net-tools package on Linux systems)

Installation

    Clone the Repository

    bash

git clone https://github.com/yourusername/MAC-address-changer.git
cd MAC-address-changer

Ensure Python 3 is Installed

Verify that Python 3 is installed on your system. You can check this by running:

bash

    python3 --version

    Install Required Packages

    Ensure you have the necessary Python packages installed. This script does not require any external Python packages, but it uses built-in modules like subprocess, argparse, re, and logging.

Usage

    Run the Script

    To run the script, you need to specify the network interface and the new MAC address. Use the following command format:

    bash

sudo python3 mac_changer.py -i <interface> -m <new_mac>

Example:

bash

sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
