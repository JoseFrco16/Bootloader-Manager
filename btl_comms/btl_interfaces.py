# Author: Jose Francisco Marti Martin
# btl_interfaces.py Bootloader interfaces manage the whole possible interface to use.

import serial

interface = 0

def btl_comms_initialize_interface(args):

    global interface 

    if args.interface == "UART":

        interface = serial.Serial(port=args.port, baudrate=args.baudrate, timeout=1)

def btl_comms_send_through_interface(data):

    global interface 
    
    interface.write(data)

def btl_comms_read_from_interface():

    global interface 

    return interface.readline()
