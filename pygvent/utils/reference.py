import weakref
from typing import Generic, T


class WeakReference(weakref.ReferenceType, Generic[T]):
    __slots__ = ()
