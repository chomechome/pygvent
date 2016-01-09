import pygame


def convert_to_mask(image):
    return pygame.mask.from_surface(image)


def fill_with_gradient(surface, initial_color, final_color, rect=None,
                       vertical=True, forward=True):
    """

    :param surface: An object to fill with gradient pattern
    :type initial_color: pygame.color.Color
    :type final_color: pygame.color.Color
    :param rect: Area to fill, defaults to whole area of given surface
    :param vertical:
    :param forward:
    """
    rect = rect or surface.get_rect()
    x1, x2 = rect.left, rect.right
    y1, y2 = rect.top, rect.bottom
    if vertical:
        h = y2 - y1
    else:
        h = x2 - x1
    if forward:
        a, b = initial_color, final_color
    else:
        b, a = initial_color, final_color
    rate = (
        float(b[0] - a[0]) / h,
        float(b[1] - a[1]) / h,
        float(b[2] - a[2]) / h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1, y2):
            initial_color = (
                min(max(a[0] + (rate[0] * (line - y1)), 0), 255),
                min(max(a[1] + (rate[1] * (line - y1)), 0), 255),
                min(max(a[2] + (rate[2] * (line - y1)), 0), 255)
            )
            fn_line(surface, initial_color, (x1, line), (x2, line))
    else:
        for col in range(x1, x2):
            initial_color = (
                min(max(a[0] + (rate[0] * (col - x1)), 0), 255),
                min(max(a[1] + (rate[1] * (col - x1)), 0), 255),
                min(max(a[2] + (rate[2] * (col - x1)), 0), 255)
            )
            fn_line(surface, initial_color, (col, y1), (col, y2))
