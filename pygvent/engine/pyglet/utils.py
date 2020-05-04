import pyglet.font.ttf


def add_font(path: str) -> str:
    info = pyglet.font.ttf.TruetypeInfo(path)
    name: str = info.get_name('family')
    info.close()

    pyglet.font.add_file(path)
    return name
