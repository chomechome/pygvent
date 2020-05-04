from pygvent.action import InstantAction, IReversible
from pygvent.actor import Actor


class Enable(InstantAction, IReversible):
    def __init__(self, target: Actor):
        super().__init__()
        self._target = target

    def do(self):
        self._target.is_enabled = True

    def reversed(self):
        return Disable(self._target)


class Disable(InstantAction, IReversible):
    def __init__(self, target: Actor):
        super().__init__()
        self._target = target

    def do(self):
        self._target.is_enabled = False

    def reversed(self):
        return Enable(self._target)


class Show(InstantAction, IReversible):
    def __init__(self, target: Actor):
        super().__init__()
        self._target = target

    def do(self):
        self._target.is_visible = True

    def reversed(self):
        return Hide(self._target)


class Hide(InstantAction, IReversible):
    def __init__(self, target: Actor):
        super().__init__()
        self._target = target

    def do(self):
        self._target.is_visible = False

    def reversed(self):
        return Show(self._target)
