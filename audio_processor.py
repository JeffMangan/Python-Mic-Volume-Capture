
import numpy as np
from config import Config

class AudioProcessor:
    def __init__(self):
        self.thresholds = [
            (Config.LOW_VOLUME, Config.LINE_COLORS["low"], 2),
            (Config.LOW_VOLUME * 2, Config.LINE_COLORS["medium"], 2),
            (Config.LOW_VOLUME * 3, Config.LINE_COLORS["high"], 2),
            (Config.LOW_VOLUME * 4, Config.LINE_COLORS["higher"], 2),
            (Config.LOW_VOLUME * 5, Config.LINE_COLORS["highest"], Config.HIGHEST_NUMBER_LINES)
        ]

    def determine_color_and_rows(self, volume):
        """Determine color and number of rows based on volume thresholds."""
        for threshold, color, rows in self.thresholds:
            if volume < threshold:
                return color, rows
        return self.thresholds[-1][1], self.thresholds[-1][2]

    def process_audio(self, indata):
        """Calculate current volume based on audio input data."""
        current_volume = np.linalg.norm(indata) * Config.LINE_LENGTH_MULTIPLIER
        current_volume = max(1, min(current_volume, Config.LOW_VOLUME * 5))
        line_text = '%s%s' + str("_" * (int(current_volume * 2.5))) + '%s'
        color, rows = self.determine_color_and_rows(current_volume)
        return line_text, color, rows
