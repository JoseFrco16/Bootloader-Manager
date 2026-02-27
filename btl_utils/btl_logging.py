# Author: Jose Francisco Marti Martin
# btl_logging.py Bootloader logger

import logging

Logger = ""

def CreateLogger():
    """
    Create logger with console and file handler
    """
    global Logger

    # Create main logger
    Logger = logging.getLogger("bootloader") 
    Logger.setLevel(logging.DEBUG)

    # --- File handler --- 
    file_handler = logging.FileHandler("bootloader.log", encoding="utf-8") 
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") 
    file_handler.setFormatter(file_format) 

    # --- Console handler --- 
    console_handler = logging.StreamHandler() 
    console_handler.setLevel(logging.DEBUG)
    console_format = logging.Formatter("[%(levelname)s] %(message)s") 
    console_handler.setFormatter(console_format)

    Logger.addHandler(file_handler) 
    Logger.addHandler(console_handler)

    return Logger

def GetLogger():
    """
    Logger getter
    """
    global Logger

    return Logger




