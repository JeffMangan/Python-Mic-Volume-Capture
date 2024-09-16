
import sounddevice as sd
from config import Config
from audio_processor import AudioProcessor
from color_manager import ColorManager

class AudioVisualizer:
    def __init__(self):
        self.audio_processor = AudioProcessor()

    def audio_callback(self, indata, frames, time, status):
        """Callback for processing audio data and printing colored lines."""
        line_text, color, rows = self.audio_processor.process_audio(indata)
        ColorManager.print_line(line_text, color, rows)

    def start(self):
        """Start the audio visualizer."""
        stream = sd.InputStream(callback=self.audio_callback)
        with stream:
            sd.sleep(Config.PAUSE_BETWEEN_LINES)
