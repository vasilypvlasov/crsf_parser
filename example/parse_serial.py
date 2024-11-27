#!/usr/bin/env python3
from operator import contains
from typing import Container
from crsf_parser import CRSFParser, PacketValidationStatus
from serial import Serial

from crsf_parser.payloads import PacketsTypes
from crsf_parser.handling import crsf_build_frame


def print_frame(frame: Container, status: PacketValidationStatus) -> None:
    print(
        f"""
    {status}
    {frame}
    """
    )


crsf_parser = CRSFParser(print_frame)
# n = 10
# v = 1
# with Serial("/dev/ttyUSB0", 425000, timeout=2) as ser:
#     input = bytearray()
#     while True:
#         # if n == 0:
#         #     n = 10
#         #     frame = crsf_build_frame(
#         #         PacketsTypes.BATTERY_SENSOR,
#         #         {"voltage": v, "current": 1, "capacity": 100, "remaining": 100},
#         #     )
#         #     v += 1
#             # ser.write(frame)
#         # n = n - 1
#         values = ser.read(100)
#         input.extend(values)
#         crsf_parser.parse_stream(input)


# input = bytearray([int(c, 16) for c in "c8 0c 14 00 00 64 05 00 01 03 00 00 00 fa".split()])
bites_str = "c8 18 16 c0 73 c5 f7 be f7 8b f2 95 af 7c e5 63 5f f9 ca 07 00 00 4c 7c e2 e9 4d 53 b0 40 31 0d 0a 4d 53 50 40 44 45 46 60 31 0d 0a 4d 53 b0 40 44 45 46 40 32 0d 0a 4d 53 50 40 4f 4b 40 31 0d 0a 4d 53 b0 40 4f 4b 40 32 0d 0a 74 6f 74 61 6c 42 75 66 66 65 72 4c 65 6e 60 38 0a 0d 0a c8 06 32 00 ef 10 03 08 c8 0c 14 06 00 64 07 00 01 03 00 00 00 61 c8 18 16 c0 73"
input = bytearray([int(c, 16) for c in bites_str.split()])
crsf_parser.parse_stream(input)