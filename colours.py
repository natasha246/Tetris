class Colours:
    dark_grey = (38,38,38)
    green = (88, 135, 68)
    red = (166, 56, 56)
    orange = (189, 97, 32)
    yellow = (201, 169, 26)
    purple = (95, 60, 120)
    cyan = (91, 154, 168)
    blue = (46, 48, 105)
    white = (255,255,255)
    light_grey = (60, 60, 60)

    @classmethod
    def get_cell_colours(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]