
class Config:
    # Constants configuration for application settings
    PAUSE_BETWEEN_LINES = 5000  # Reduced number to make it more reasonable
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
