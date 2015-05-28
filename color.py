

class color:
    """Color ANSI codes"""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Colorize:
    """Color ANSI codes"""
    colors = {
        'PURPLE': '\033[95m',
        'CYAN': '\033[96m',
        'DARKCYAN': '\033[36m',
        'BLUE': '\033[94m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'RED': '\033[91m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'END': '\033[0m',
        'DIRECTION': '\033[92m',  # FG_GREEN
        'COMMAND': '\033[41m',    # BG_RED
        'LOCATION': '\033[94m',   # FG_BLUE
    }

    @classmethod
    def colorize(self, color, text):
        return ('{}{}{}'.format(self.colors[color], text, self.colors['END']))
