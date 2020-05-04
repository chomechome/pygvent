from typing import Optional

from pygvent.utils.slots import Slots


class Matrix(Slots):
    __slots__ = 'm11', 'm12', 'm13', 'm21', 'm22', 'm23', 'm31', 'm32', 'm33'

    def __init__(self,
                 m11: float = 1, m12: float = 0, m13: float = 0,
                 m21: float = 0, m22: float = 1, m23: float = 0,
                 m31: float = 0, m32: float = 0, m33: float = 1,
                 ):
        self.m11, self.m12, self.m13 = m11, m12, m13
        self.m21, self.m22, self.m23 = m21, m22, m23
        self.m31, self.m32, self.m33 = m31, m32, m33

    @property
    def determinant(self):
        m11, m12, m13 = self.m11, self.m12, self.m13
        m21, m22, m23 = self.m21, self.m22, self.m23
        m31, m32, m33 = self.m31, self.m32, self.m33

        return (m11 * m22 * m33 + m12 * m23 * m31 + m13 * m21 * m32 -
                m11 * m23 * m32 - m12 * m21 * m33 - m13 * m22 * m31)

    def __repr__(self):
        return (
            'Matrix([{: .2f} {: .2f} {: .2f}\n'
            '        {: .2f} {: .2f} {: .2f}\n'
            '        {: .2f} {: .2f} {: .2f}])'.format(
                self.m11, self.m12, self.m13,
                self.m21, self.m22, self.m23,
                self.m31, self.m32, self.m33,
            )
        )

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        a11, a12, a13 = self.m11, self.m12, self.m13
        a21, a22, a23 = self.m21, self.m22, self.m23
        a31, a32, a33 = self.m31, self.m32, self.m33

        b11, b12, b13 = other.m11, other.m12, other.m13
        b21, b22, b23 = other.m21, other.m22, other.m23
        b31, b32, b33 = other.m31, other.m32, other.m33

        return Matrix(
            a11 * b11 + a12 * b21 + a13 * b31,
            a11 * b12 + a12 * b22 + a13 * b32,
            a11 * b13 + a12 * b23 + a13 * b33,

            a21 * b11 + a22 * b21 + a23 * b31,
            a21 * b12 + a22 * b22 + a23 * b32,
            a21 * b13 + a22 * b23 + a23 * b33,

            a31 * b11 + a32 * b21 + a33 * b31,
            a31 * b12 + a32 * b22 + a33 * b32,
            a31 * b13 + a32 * b23 + a33 * b33,
        )

    def __imul__(self, other: 'Matrix') -> 'Matrix':
        a11, a12, a13 = self.m11, self.m12, self.m13
        a21, a22, a23 = self.m21, self.m22, self.m23
        a31, a32, a33 = self.m31, self.m32, self.m33

        b11, b12, b13 = other.m11, other.m12, other.m13
        b21, b22, b23 = other.m21, other.m22, other.m23
        b31, b32, b33 = other.m31, other.m32, other.m33

        self.m11 = a11 * b11 + a12 * b21 + a13 * b31
        self.m12 = a11 * b12 + a12 * b22 + a13 * b32
        self.m13 = a11 * b13 + a12 * b23 + a13 * b33

        self.m21 = a21 * b11 + a22 * b21 + a23 * b31
        self.m22 = a21 * b12 + a22 * b22 + a23 * b32
        self.m23 = a21 * b13 + a22 * b23 + a23 * b33

        self.m31 = a31 * b11 + a32 * b21 + a33 * b31
        self.m32 = a31 * b12 + a32 * b22 + a33 * b32
        self.m33 = a31 * b13 + a32 * b23 + a33 * b33
        return self

    def __copy__(self):
        return Matrix(
            self.m11, self.m12, self.m13,
            self.m21, self.m22, self.m23,
            self.m31, self.m32, self.m33,
        )

    copy = __copy__

    def invert(self) -> Optional['Matrix']:
        determinant = self.determinant
        if determinant == 0:
            return None

        return Matrix()
