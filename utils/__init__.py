def is_subscriptable(other):
    return hasattr(other, "__getitem__")
