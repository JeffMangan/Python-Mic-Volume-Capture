import numpy as np
import sounddevice as sd
from colored import fg, bg, attr
import time as t

class Config:
    # Constants configuration for application settings
    PAUSE_BETWEEN_LINES = 5 * 10000000000000  # unusually large number, consider reducing
    LINE_LENGTH_MULTIPLIER = 10
    HIGHEST_NUMBER_LINES = 100
    LOW_VOLUME = 15
    COLORS = {
        "green": 2,
        "blue": 4,
        "yellow": 226,
        "purple": 54,
        "magenta": 5,
        "orange": 208,
        "red": 9,
        "dark_red": 124
    }
    LINE_COLORS = {
        "low": COLORS["blue"],
        "medium": COLORS["green"],
        "high": COLORS["yellow"],
        "higher": COLORS["orange"],
        "highest": COLORS["red"]
    }

class AudioVisualizer:
    def __init__(self):
        self.thresholds = [
            (Config.LOW_VOLUME, Config.LINE_COLORS["low"], 2),
            (Config.LOW_VOLUME * 2, Config.LINE_COLORS["medium"], 2),
            (Config.LOW_VOLUME * 3, Config.LINE_COLORS["high"], 2),
            (Config.LOW_VOLUME * 4, Config.LINE_COLORS["higher"], 2),
            (Config.LOW_VOLUME * 5, Config.LINE_COLORS["highest"], Config.HIGHEST_NUMBER_LINES)
        ]

    def print_line(self, txt, color, num_of_rows):
        # Print colored text lines based on volume
        for _ in range(num_of_rows):
            print(txt % (fg(color), bg(color), attr(0)))
        t.sleep(0)  # Non-blocking, but allows for time.sleep if needed

    def determine_color_and_rows(self, volume):
        # Determine color and number of rows based on volume thresholds
        for threshold, color, rows in self.thresholds:
            if volume < threshold:
                return color, rows
        return self.thresholds[-1][1], self.thresholds[-1][2]

    def audio_callback(self, indata, frames, time, status):
        # Callback for processing audio data
        current_volume = np.linalg.norm(indata) * Config.LINE_LENGTH_MULTIPLIER
        current_volume = max(1, min(current_volume, Config.LOW_VOLUME * 5))
        line_text = '%s%s' + str("_" * (int(current_volume * 2.5))) + '%s'
        color, rows = self.determine_color_and_rows(current_volume)
        self.print_line(line_text, color, rows)

if __name__ == "__main__":
    visualizer = AudioVisualizer()
    stream = sd.InputStream(callback=visualizer.audio_callback)
    with stream:
        sd.sleep(Config.PAUSE_BETWEEN_LINES)
