# Print out realtime audio volume as ascii bars
import sys
import traceback

import numpy as np
import sounddevice as sd

from colored import fg, bg, attr


duration: int = 100
i = 0

# https://pypi.org/project/colored/
green = 2
blue = 4
yellow = 226
purple = 54
magenta = 5
orange = 208
red = 9
dark_red = 1

low = blue
medium = green
high = yellow
extreme = orange
max = red





lowVolume = 10
mediumVolume = lowVolume*2
warningVolume = lowVolume*3
highVolume = lowVolume*4
maxVolume = lowVolume*5

x = '%s%s' + str(int(20)) + str("=" * (int(20 * 2.5))) + '%s'
# print(x % (fg(low), bg(low), attr(0)))
# print(x % (fg(medium), bg(medium), attr(0)))
# print(x % (fg(warning), bg(warning), attr(0)))
# print(x % (fg(high), bg(high), attr(0)))
# print(x % (fg(max), bg(max), attr(0)))
# sys.exit(0)


def audio_callback(indata, frames, time, status):
    global i
    while i < 100:
        i = i + 1
        return
    currentVolume = np.linalg.norm(indata) * 10
    # print(str(int(volume_norm)))
    display_length = currentVolume
    if currentVolume > maxVolume:
        display_length = highVolume*1.2

    x = '%s%s' + str(int(display_length)) + str("=" * (int(display_length*2.5))) + '%s'
    if currentVolume > maxVolume:
        print(x % (fg(max), bg(max), attr(0)))
        print(x % (fg(max), bg(max), attr(0)))
        print(x % (fg(max), bg(max), attr(0)))
        print(x % (fg(max), bg(max), attr(0)))
        print(x % (fg(max), bg(max), attr(0)))
    elif currentVolume < lowVolume:
        # x = '%s%s' + str("=" * int(volume_norm)) + '%s'
        # print(low)
        print(x % (fg(low), bg(low), attr(0)))
        print(x % (fg(low), bg(low), attr(0)))
    # elif volume_norm < 51:
        # x = '%s%s' + str("=" * int(volume_norm)) + '%s'
        # print(x % (fg(yellow), bg(yellow), attr(0)))
    elif currentVolume < mediumVolume:
        # x = '%s%s' + str("=" * int(volume_norm)) + '%s'
        # print(medium)
        print(x % (fg(medium), bg(medium), attr(0)))
        print(x % (fg(medium), bg(medium), attr(0)))
    # elif volume_norm < 200:
        # print(Colors.PINK + str(int(volume_norm)), "_", "=" * int(volume_norm) + Colors.PINK)
        # print(x % (fg(magenta), bg(magenta), attr(0)))
    elif currentVolume < warningVolume:
        # x = '%s%s' + str("=" * int(volume_norm)) + '%s'
        # print(warning)
        print(x % (fg(high), bg(high), attr(0)))
        print(x % (fg(high), bg(high), attr(0)))
    else:
        # x = '%s%s' + str("=" * int(volume_norm)) + '%s'
        # print(high)
        print(x % (fg(extreme), bg(extreme), attr(0)))
        print(x % (fg(extreme), bg(extreme), attr(0)))


stream = sd.InputStream(callback=audio_callback)
with stream:
    sd.sleep(duration * 100000000)
