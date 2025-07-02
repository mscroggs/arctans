"""Arctans."""

from typing import Any
import math
import sympy
from sympy.core.expr import Expr


class ArctanSum:
    """The sum of some arctans."""

    def __init__(self, *terms: tuple[Any, Any]):
        """Initialise."""
        terms_dict = {}
        for c, a in terms:
            c = sympy.S(c)
            a = sympy.S(a)
            if a.is_infinite:
                a = sympy.Integer(1)
                c *= 2
            if not a.is_infinite and a < 0:
                a *= -1
                c *= -1
            if a not in terms_dict:
                terms_dict[a] = sympy.Integer(0)
            terms_dict[a] += c
        self._terms = [(j, i) for i, j in terms_dict.items()]
        maxa = max(j for i, j in self._terms if not j.is_infinite)
        self._terms.sort(key=lambda i: 2 * maxa if i[1].is_infinite else i[1])
        assert len(set([i[1] for i in self._terms])) == len([i[1] for i in self._terms])

    def __repr__(self) -> str:
        """Representation."""
        return self.__str__()

    def __str__(self) -> str:
        """Convert to a string."""
        return "ArctanSum(" + " + ".join(f"{i}[{j}]" for i, j in self._terms) + ")"

    def __float__(self) -> float:
        """Convert to a float."""
        return sum(float(i) * (math.pi / 2 if j.is_infinite else math.atan(float(j))) for i, j in self._terms)

    def __mul__(self, other):
        """Multiply."""
        try:
            s_o = sympy.S(other)
            return ArctanSum(*[
                (s_o * i, j) for i, j in self.terms
            ])
        except sympy.SympifyError:
            return NotImplemented

    def __rmul__(self, other):
        """Multiply from the right."""
        try:
            s_o = sympy.S(other)
            return ArctanSum(*[
                (i * s_o, j) for i, j in self.terms
            ])
        except sympy.SympifyError:
            return NotImplemented

    def __add__(self, other):
        """Add."""
        if isinstance(other, ArctanSum):
            return ArctanSum(*self.terms, *other.terms)
        else:
            return NotImplemented

    def __sub__(self, other):
        """Subtract."""
        if isinstance(other, ArctanSum):
            return ArctanSum(*self.terms, *[(-i, j) for i, j in other.terms])
        else:
            return NotImplemented

    @property
    def nterms(self) -> int:
        """Number of terms."""
        return len(self._terms)

    @property
    def terms(self) -> list[tuple[Expr, Expr]]:
        """Terms."""
        return self._terms
