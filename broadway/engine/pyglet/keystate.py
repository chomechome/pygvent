import pyglet

from broadway.input.keys import IKeyState
from broadway.input.keys import Key


class PygletKeyState(IKeyState):

    _KEY_CODES = {
        Key.ZERO: pyglet.window.key._0,
        Key.ONE: pyglet.window.key._1,
        Key.TWO: pyglet.window.key._2,
        Key.THREE: pyglet.window.key._3,
        Key.FOUR: pyglet.window.key._4,
        Key.FIVE: pyglet.window.key._5,
        Key.SIX: pyglet.window.key._6,
        Key.SEVEN: pyglet.window.key._7,
        Key.EIGHT: pyglet.window.key._8,
        Key.NINE: pyglet.window.key._9,

        Key.A: pyglet.window.key.A,
        Key.B: pyglet.window.key.B,
        Key.C: pyglet.window.key.C,
        Key.D: pyglet.window.key.D,
        Key.E: pyglet.window.key.E,
        Key.F: pyglet.window.key.F,
        Key.G: pyglet.window.key.G,
        Key.H: pyglet.window.key.H,
        Key.I: pyglet.window.key.I,
        Key.J: pyglet.window.key.J,
        Key.K: pyglet.window.key.K,
        Key.L: pyglet.window.key.L,
        Key.M: pyglet.window.key.M,
        Key.N: pyglet.window.key.N,
        Key.O: pyglet.window.key.O,
        Key.P: pyglet.window.key.P,
        Key.Q: pyglet.window.key.Q,
        Key.R: pyglet.window.key.R,
        Key.S: pyglet.window.key.S,
        Key.T: pyglet.window.key.T,
        Key.U: pyglet.window.key.U,
        Key.V: pyglet.window.key.V,
        Key.W: pyglet.window.key.W,
        Key.X: pyglet.window.key.X,
        Key.Y: pyglet.window.key.Y,
        Key.Z: pyglet.window.key.Z,

        Key.UP: pyglet.window.key.UP,
        Key.DOWN: pyglet.window.key.DOWN,
        Key.LEFT: pyglet.window.key.LEFT,
        Key.RIGHT: pyglet.window.key.RIGHT,

        Key.LEFT_ALT: pyglet.window.key.LALT,
        Key.LEFT_CTRL: pyglet.window.key.LCTRL,
        Key.LEFT_SHIFT: pyglet.window.key.LSHIFT,

        Key.RIGHT_ALT: pyglet.window.key.RALT,
        Key.RIGHT_CTRL: pyglet.window.key.RCTRL,
        Key.RIGHT_SHIFT: pyglet.window.key.RSHIFT,

        Key.LEFT_BRACKET: pyglet.window.key.BRACKETLEFT,
        Key.LEFT_PARENTHESIS: pyglet.window.key.PARENLEFT,

        Key.RIGHT_BRACKET: pyglet.window.key.BRACKETRIGHT,
        Key.RIGHT_PARENTHESIS: pyglet.window.key.PARENRIGHT,

        Key.F1: pyglet.window.key.F1,
        Key.F2: pyglet.window.key.F2,
        Key.F3: pyglet.window.key.F3,
        Key.F4: pyglet.window.key.F4,
        Key.F5: pyglet.window.key.F5,
        Key.F6: pyglet.window.key.F6,
        Key.F7: pyglet.window.key.F7,
        Key.F8: pyglet.window.key.F8,
        Key.F9: pyglet.window.key.F9,
        Key.F10: pyglet.window.key.F10,
        Key.F11: pyglet.window.key.F11,
        Key.F12: pyglet.window.key.F12,

        Key.NUMPAD_ZERO: pyglet.window.key.NUM_0,
        Key.NUMPAD_ONE: pyglet.window.key.NUM_1,
        Key.NUMPAD_TWO: pyglet.window.key.NUM_2,
        Key.NUMPAD_THREE: pyglet.window.key.NUM_3,
        Key.NUMPAD_FOUR: pyglet.window.key.NUM_4,
        Key.NUMPAD_FIVE: pyglet.window.key.NUM_5,
        Key.NUMPAD_SIX: pyglet.window.key.NUM_6,
        Key.NUMPAD_SEVEN: pyglet.window.key.NUM_7,
        Key.NUMPAD_EIGHT: pyglet.window.key.NUM_8,
        Key.NUMPAD_NINE: pyglet.window.key.NUM_9,

        Key.NUMPAD_DIVIDE: pyglet.window.key.NUM_DIVIDE,
        Key.NUMPAD_ENTER: pyglet.window.key.NUM_ENTER,
        Key.NUMPAD_EQUALS: pyglet.window.key.NUM_EQUAL,
        Key.NUMPAD_SUBTRACT: pyglet.window.key.NUM_SUBTRACT,
        Key.NUMPAD_MULTIPLY: pyglet.window.key.NUM_MULTIPLY,
        Key.NUMPAD_PERIOD: pyglet.window.key.NUM_DECIMAL,
        Key.NUMPAD_PLUS: pyglet.window.key.NUM_ADD,

        Key.AMPERSAND: pyglet.window.key.AMPERSAND,
        Key.ASTERISK: pyglet.window.key.ASTERISK,
        Key.AT: pyglet.window.key.AT,

        Key.BACKQUOTE: pyglet.window.key.QUOTELEFT,
        Key.BACKSLASH: pyglet.window.key.BACKSLASH,
        Key.BACKSPACE: pyglet.window.key.BACKSPACE,
        Key.BREAK: pyglet.window.key.BREAK,

        Key.CAPSLOCK: pyglet.window.key.CAPSLOCK,
        Key.CARET: pyglet.window.key.ASCIICIRCUM,
        Key.CLEAR: pyglet.window.key.CLEAR,
        Key.COLON: pyglet.window.key.COLON,
        Key.COMMA: pyglet.window.key.COMMA,

        Key.DELETE: pyglet.window.key.DELETE,
        Key.DOLLAR: pyglet.window.key.DOLLAR,

        Key.END: pyglet.window.key.END,
        Key.ENTER: pyglet.window.key.ENTER,
        Key.EQUALS: pyglet.window.key.EQUAL,
        Key.ESCAPE: pyglet.window.key.ESCAPE,
        Key.EXCLAIM: pyglet.window.key.EXCLAMATION,

        Key.GREATER: pyglet.window.key.GREATER,

        Key.HASH: pyglet.window.key.HASH,
        Key.HELP: pyglet.window.key.HELP,
        Key.HOME: pyglet.window.key.HOME,

        Key.INSERT: pyglet.window.key.INSERT,

        Key.LESS: pyglet.window.key.LESS,

        Key.MENU: pyglet.window.key.MENU,
        Key.MINUS: pyglet.window.key.MINUS,

        Key.NUMLOCK: pyglet.window.key.NUMLOCK,

        Key.PAGEDOWN: pyglet.window.key.PAGEDOWN,
        Key.PAGEUP: pyglet.window.key.PAGEUP,
        Key.PAUSE: pyglet.window.key.PAUSE,
        Key.PERIOD: pyglet.window.key.PERIOD,
        Key.PLUS: pyglet.window.key.PLUS,
        Key.PRINT: pyglet.window.key.PRINT,

        Key.QUESTION: pyglet.window.key.QUESTION,
        Key.QUOTE: pyglet.window.key.APOSTROPHE,
        Key.QUOTE_DOUBLE: pyglet.window.key.DOUBLEQUOTE,

        Key.SCROLLOCK: pyglet.window.key.SCROLLLOCK,
        Key.SEMICOLON: pyglet.window.key.SEMICOLON,
        Key.SLASH: pyglet.window.key.SLASH,
        Key.SPACE: pyglet.window.key.SPACE,

        Key.TAB: pyglet.window.key.TAB,

        Key.UNDERSCORE: pyglet.window.key.UNDERSCORE,
    }

    def __init__(self, handler: pyglet.window.key.KeyStateHandler):
        self._handler = handler
        self._state = handler.copy()

    def update(self):
        self._state = self._handler.copy()

    def is_up(self, key: Key) -> bool:
        code = self._KEY_CODES[key]
        return not self._state.get(code, False)

    def is_down(self, key: Key) -> bool:
        code = self._KEY_CODES[key]
        return self._state.get(code, False)
