# Author: JoseFrco16
# btl_manager.py Bootloader manager establish communication with the MCU bootloader.

import argparse
import sys
import btl_comms
import btl_utils

def cli():
    """
    Command line interface using argaparse module
    """
    cli = argparse.ArgumentParser(description='Bootloader host manager')
    cli.add_argument('-i', 
                     '--interface',
                     type=str,
                     required=True,
                     choices=["UART"],
                     help='Interface used in the bootloader communication')
    cli.add_argument('-p',
                     '--port',
                     type=str,
                     required=(('--interface=UART' in sys.argv) or ('-i=UART' in sys.argv)),
                     help='USB Communication Port')
    cli.add_argument('-b',
                     '--baudrate',
                     type=int,
                     required=(('--interface=UART' in sys.argv) or ('-i=UART' in sys.argv)),
                     choices=[2400, 4800, 9600, 38400, 115200],
                     help='UART Baudrate, it must match the configured in SLAVE')

    return cli.parse_args()

def cli_runtime(args):
    """
    Command line interface for slave communication
    """
    while True:

        cmd = input(">> ")

        if cmd == "exit":

            break

        elif cmd in btl_comms.CommandMap.keys():

            btl_comms.cmd_handler(cmd)

        else:

            print("manage error") 

def main():
    """
    btl_manager script entry point
    """
    # The idea is to manage the bootloader from exportable class in btl_class
    
    btl_utils.CreateLogger()
    Logger = btl_utils.GetLogger()
    Logger.info("--- Bootloader Manager ---")

    args = cli()
    cli_runtime(args)

if __name__ == "__main__":

    main()