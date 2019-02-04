import pygame

from broadway.input.keys import Key, IKeyState


class PygameKeyState(IKeyState):

    _KEY_CODES = {
        Key.ZERO: pygame.K_0,
        Key.ONE: pygame.K_1,
        Key.TWO: pygame.K_2,
        Key.THREE: pygame.K_3,
        Key.FOUR: pygame.K_4,
        Key.FIVE: pygame.K_5,
        Key.SIX: pygame.K_6,
        Key.SEVEN: pygame.K_7,
        Key.EIGHT: pygame.K_8,
        Key.NINE: pygame.K_9,

        Key.A: pygame.K_a,
        Key.B: pygame.K_b,
        Key.C: pygame.K_c,
        Key.D: pygame.K_d,
        Key.E: pygame.K_e,
        Key.F: pygame.K_f,
        Key.G: pygame.K_g,
        Key.H: pygame.K_h,
        Key.I: pygame.K_i,
        Key.J: pygame.K_j,
        Key.K: pygame.K_k,
        Key.L: pygame.K_l,
        Key.M: pygame.K_m,
        Key.N: pygame.K_n,
        Key.O: pygame.K_o,
        Key.P: pygame.K_p,
        Key.Q: pygame.K_q,
        Key.R: pygame.K_r,
        Key.S: pygame.K_s,
        Key.T: pygame.K_t,
        Key.U: pygame.K_u,
        Key.V: pygame.K_v,
        Key.W: pygame.K_w,
        Key.X: pygame.K_x,
        Key.Y: pygame.K_y,
        Key.Z: pygame.K_z,

        Key.UP: pygame.K_UP,
        Key.DOWN: pygame.K_DOWN,
        Key.LEFT: pygame.K_LEFT,
        Key.RIGHT: pygame.K_RIGHT,

        Key.LEFT_ALT: pygame.K_LALT,
        Key.LEFT_CTRL: pygame.K_LCTRL,
        Key.LEFT_SHIFT: pygame.K_LSHIFT,

        Key.RIGHT_ALT: pygame.K_RALT,
        Key.RIGHT_CTRL: pygame.K_RCTRL,
        Key.RIGHT_SHIFT: pygame.K_RSHIFT,

        Key.LEFT_BRACKET: pygame.K_LEFTBRACKET,
        Key.LEFT_PARENTHESIS: pygame.K_LEFTPAREN,

        Key.RIGHT_BRACKET: pygame.K_RIGHTBRACKET,
        Key.RIGHT_PARENTHESIS: pygame.K_RIGHTPAREN,

        Key.F1: pygame.K_F1,
        Key.F2: pygame.K_F2,
        Key.F3: pygame.K_F3,
        Key.F4: pygame.K_F4,
        Key.F5: pygame.K_F5,
        Key.F6: pygame.K_F6,
        Key.F7: pygame.K_F7,
        Key.F8: pygame.K_F8,
        Key.F9: pygame.K_F9,
        Key.F10: pygame.K_F10,
        Key.F11: pygame.K_F11,
        Key.F12: pygame.K_F12,

        Key.NUMPAD_ZERO: pygame.K_KP0,
        Key.NUMPAD_ONE: pygame.K_KP1,
        Key.NUMPAD_TWO: pygame.K_KP2,
        Key.NUMPAD_THREE: pygame.K_KP3,
        Key.NUMPAD_FOUR: pygame.K_KP4,
        Key.NUMPAD_FIVE: pygame.K_KP5,
        Key.NUMPAD_SIX: pygame.K_KP6,
        Key.NUMPAD_SEVEN: pygame.K_KP7,
        Key.NUMPAD_EIGHT: pygame.K_KP8,
        Key.NUMPAD_NINE: pygame.K_KP9,

        Key.NUMPAD_DIVIDE: pygame.K_KP_DIVIDE,
        Key.NUMPAD_ENTER: pygame.K_KP_ENTER,
        Key.NUMPAD_EQUALS: pygame.K_KP_EQUALS,
        Key.NUMPAD_SUBTRACT: pygame.K_KP_MINUS,
        Key.NUMPAD_MULTIPLY: pygame.K_KP_MULTIPLY,
        Key.NUMPAD_PERIOD: pygame.K_KP_PERIOD,
        Key.NUMPAD_PLUS: pygame.K_KP_PLUS,

        Key.AMPERSAND: pygame.K_AMPERSAND,
        Key.ASTERISK: pygame.K_ASTERISK,
        Key.AT: pygame.K_AT,

        Key.BACKQUOTE: pygame.K_BACKQUOTE,
        Key.BACKSLASH: pygame.K_BACKSLASH,
        Key.BACKSPACE: pygame.K_BACKSPACE,
        Key.BREAK: pygame.K_BREAK,

        Key.CAPSLOCK: pygame.K_CAPSLOCK,
        Key.CARET: pygame.K_CARET,
        Key.CLEAR: pygame.K_CLEAR,
        Key.COLON: pygame.K_COLON,
        Key.COMMA: pygame.K_COMMA,

        Key.DELETE: pygame.K_DELETE,
        Key.DOLLAR: pygame.K_DOLLAR,

        Key.END: pygame.K_END,
        Key.ENTER: pygame.K_RETURN,
        Key.EQUALS: pygame.K_EQUALS,
        Key.ESCAPE: pygame.K_ESCAPE,
        Key.EXCLAIM: pygame.K_EXCLAIM,

        Key.GREATER: pygame.K_GREATER,

        Key.HASH: pygame.K_HASH,
        Key.HELP: pygame.K_HELP,
        Key.HOME: pygame.K_HOME,

        Key.INSERT: pygame.K_INSERT,

        Key.LESS: pygame.K_LESS,

        Key.MENU: pygame.K_MENU,
        Key.MINUS: pygame.K_MINUS,

        Key.NUMLOCK: pygame.K_NUMLOCK,

        Key.PAGEDOWN: pygame.K_PAGEDOWN,
        Key.PAGEUP: pygame.K_PAGEUP,
        Key.PAUSE: pygame.K_PAUSE,
        Key.PERIOD: pygame.K_PERIOD,
        Key.PLUS: pygame.K_PLUS,
        Key.PRINT: pygame.K_PRINT,

        Key.QUESTION: pygame.K_QUESTION,
        Key.QUOTE: pygame.K_QUOTE,
        Key.QUOTE_DOUBLE: pygame.K_QUOTEDBL,

        Key.SCROLLOCK: pygame.K_SCROLLOCK,
        Key.SEMICOLON: pygame.K_SEMICOLON,
        Key.SLASH: pygame.K_SLASH,
        Key.SPACE: pygame.K_SPACE,

        Key.TAB: pygame.K_TAB,

        Key.UNDERSCORE: pygame.K_UNDERSCORE,
    }

    def __init__(self):
        self._state = pygame.key.get_pressed()

    def update(self):
        self._state = pygame.key.get_pressed()

    def is_up(self, key: Key) -> bool:
        code = self._KEY_CODES[key]
        return not self._state[code]

    def is_down(self, key: Key) -> bool:
        code = self._KEY_CODES[key]
        return self._state[code]
