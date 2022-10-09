# Print out realtime audio volume as ascii bars
import numpy as np
import sounddevice as sd
from colored import fg, bg, attr
import time as t

# does not seem to be accurate, but too low will cause code to crash after a while
pause_between_lines = 5 * 10000000000000

# https://pypi.org/project/colored/
#################### choices of colors to use ####################
green = 2
blue = 4
yellow = 226
purple = 54
magenta = 5
orange = 208
red = 9
dark_red = 124
#################### actual line colors chosen ####################
low = blue
medium = green
high = yellow
higher = orange
highest = red
#################### multiplier for line to extend by x number of chars ####################
line_length_multiplier = 10
#################### number of lines to print for highest to make it more noticeable ####################
highest_number_lines = 100
#################### volume max for each category ####################
lowVolume = 15
mediumVolume = lowVolume*2
high_volume = lowVolume * 3
higher_volume = lowVolume * 4
highest_volume = lowVolume * 5

# pints the lines for each volume measurement
def print_line(txt, color, attr, num_of_rows, pause_in_seconds):
    i = 1
    while i <= num_of_rows:
        print(txt % (fg(color), bg(color), attr))
        i += 1
    t.sleep(pause_in_seconds)
    return

def audio_callback(indata, frames, time, status):
    current_volume = np.linalg.norm(indata) * line_length_multiplier
    if current_volume < 1:
        current_volume = 1
    if current_volume >= highest_volume:
        current_volume = highest_volume

    # line_text = '%s%s' + str(int(current_volume)) + str("=" * (int(current_volume*2.5))) + '%s'
    line_text = '%s%s' + str("_" * (int(current_volume*2.5))) + '%s'

    if current_volume >= highest_volume:
        print_line(line_text, highest, attr(0), highest_number_lines, 2)
    elif current_volume < lowVolume:
        print_line(line_text, low, attr(0), 2, 0)
    elif current_volume < mediumVolume:
        print_line(line_text, medium, attr(0), 2, 0)
    elif current_volume < high_volume:
        print_line(line_text, high, attr(0), 2, 0)
    else:
        print_line(line_text, higher, attr(0), 2, 0)

stream = sd.InputStream(callback=audio_callback)
with stream:
   sd.sleep(pause_between_lines) # * 100000000)
