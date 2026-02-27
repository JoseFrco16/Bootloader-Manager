# Author: Jose Francisco Marti Martin
# btl_protocol.py Bootloader protocol script implements the frame used in the communication with the MCU

from enum import Enum  
import struct

class Cmd(Enum):
    """
    Bootloader protocol commands
    """
    PING = 1
    VERSION = 2
    DEVICE_INFO = 3
    ERASE_FLASH = 4
    WRITE_FLASH = 5
    COMPUTE_CRC = 6
    AUTHENTICATE = 7
    UNLOCK = 8
    JUMP_TO_APP = 9
    RESET = 10

CommandMap = {
    "ping": Cmd.PING,
    "version": Cmd.VERSION,
    "device info": Cmd.DEVICE_INFO,
    "erase flash": Cmd.ERASE_FLASH,
    "write flash": Cmd.WRITE_FLASH,
    "compute crc": Cmd.COMPUTE_CRC,
    "authenticate": Cmd.AUTHENTICATE,
    "jump to app": Cmd.JUMP_TO_APP,
    "reset": Cmd.RESET,
}

class FramePcMcu:
    """
    Bootloader PC to MCU protocol frame class
    Frame: PC -> MCU: | SOF | CMD | LEN | DATA | CRC |
    Where:
        - SOF: Start of Frame
        - CMD: Bootloader command
        - LEN: Data length
        - DATA: Data
        - CRC: Cyclic Redundancy Check
    """
    def __init__(self, cmd: int, data: bytes):

        self.sof = 0xAA
        self.cmd = cmd
        self.len = len(data)
        self.data = data
        #self.crc = self.calc_crc()

    def calc_crc(self):

        return (self.cmd + self.len + sum(self.data)) & 0xFF

    def encode(self) -> bytes:

        return struct.pack(
            f"!BBB{self.len}s", # To add B at the end if crc is added
            self.sof,
            self.cmd,
            self.len,
            self.data,
            #self.crc
        )

class FrameMcuPc:
    """
    Bootloader MCU to PC protocol frame class
    Frame: MCU -> PC: | ACK | STATUS | LEN | DATA |
    Where:
        - ACK: Acknowledge
        - STATUS: MCU Status
        - LEN: Data length
        - DATA: Data
    """
    def __init__(self, raw: int):

        self.sof = 0xAA
        self.cmd = cmd
        self.len = len(data)
        self.data = data
        #self.crc = self.calc_crc()

    @staticmethod
    def __decode(raw: bytes):
        
        sof, cmd, length = struct.unpack("!BBB", raw[:3])
        data = raw[3:3+length]
        crc = raw[3+length]
        return Frame(cmd, data)


def cmd_handler(cmd):
    """
    Protocol command handler
    """
    frame_builder = FramePcMcu(CommandMap[cmd].value, bytes(0))
    frame = frame_builder.encode()

    return frame


if __name__ == "__main__":
    
    print(cmd_handler("ping"))
