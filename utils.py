import os

MDIR = os.path.split(os.path.abspath(__file__))[0]
ADIR = os.path.join(MDIR, 'assets')

BACKGROUND = (23, 32, 41)
COLORKEY = (255, 0, 255)


def asset(filename):
    return os.path.join(ADIR, filename)
