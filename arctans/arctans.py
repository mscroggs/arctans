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
        for i, j in self._terms:
            print(f"{i} * arctan({j})")
            print(i * math.atan(j))
        return sum(float(i) * math.atan(float(j)) for i, j in self._terms)

    @property
    def nterms(self) -> int:
        """Number of terms."""
        return len(self._terms)

    @property
    def terms(self) -> list[tuple[Expr, Expr]]:
        """Terms."""
        return self._terms
