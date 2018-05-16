

import sender

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

def func():
    getch = _Getch()
    right = False
    left = False
    key = int(getch())
    if key == 6:
        return "right"
    elif key == 4:
        return "left"
    elif key == 8:
        return "straight"
    elif key == 2:
        return "other"
    elif key == 5:
        return "stop"
    elif key == 9:
        return "pict"

host = "192.168.0.129"
sender.transmission(host, func)
