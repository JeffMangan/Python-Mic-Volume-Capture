
from colored import fg, bg, attr
import time as t

class ColorManager:
    @staticmethod
    def print_line(txt, color, num_of_rows):
        """Print colored text lines based on volume."""
        for _ in range(num_of_rows):
            print(txt % (fg(color), bg(color), attr(0)))
        t.sleep(0)  # Non-blocking, but allows for time.sleep if needed
