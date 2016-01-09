from collections import namedtuple


class Resolution(object):
    Custom = namedtuple('CustomResolution', ['width', 'height'])

    STANDARD = Custom(640, 480)
    FULL_HD = Custom(1920, 1080)
    HD_PLUS = Custom(1600, 1200)
    HD = Custom(1366, 768)
