#!/usr/bin/env python

"""
/sys/class/backlight/amdgpu_bl1/actual_brightness
"""

import argparse


def write(value):
    with open('/sys/class/backlight/amdgpu_bl1/brightness', 'w') as file:
        file.write(str(value))


def get_maximum_brightness() -> int:
    with open('/sys/class/backlight/amdgpu_bl1/max_brightness', 'r') as file:
        return int(file.read())


def parse():
    parser = argparse.ArgumentParser(description='Set the brightness value of your screen')
    parser.add_argument('brightness', type=int, nargs=1,
                        help='A brightness value between 0 and 100%')
    args = parser.parse_args()
    given_brightness = args.brightness[0]
    if not (0 <= given_brightness <= 100):
        raise ValueError("Brightness must be between 0 and 100%")
    return given_brightness


def to_absolute_brightness(relative_brightness: int):
    maximum_brightness = get_maximum_brightness()
    absolute_brightness = relative_brightness * maximum_brightness / 100
    rounded_down_absolute_brightness = int(absolute_brightness)
    return rounded_down_absolute_brightness


if __name__ == '__main__':
    relative_brightness = parse()
    absolute_brightness = to_absolute_brightness(relative_brightness)
    write(absolute_brightness)
    print(f"Brightness set to {relative_brightness}%")
