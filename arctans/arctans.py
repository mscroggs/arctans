from typing import Any
import math
import sympy


class ArctanSum:
    """The sum of some arctans."""

    def __init__(self, *terms: tuple[Any, Any]):
        self._terms = [(sympy.S(i), sympy.S(j)) for i, j in terms]
        self._terms.sort(key=lambda i: i[1])
        assert len(set([i[1] for i in self._terms])) == len([i[1] for i in self._terms])

    def __str__(self):
        return "ArctanSum(" + " + ".join(f"{i}[{j}]" for i, j in self._terms) + ")"

    def __float__(self):
        return sum(float(i) * math.atan(float(j)) for i, j in self._terms)

    @property
    def nterms(self):
        return len(self._terms)

    @property
    def terms(self):
        return self._terms
