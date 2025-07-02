from math import pi
import sympy
from arctans import ArctanSum
from utils import isclose


def test_simplify():
    s = ArctanSum((1, 5), (2, 5))
    assert s.nterms == 1
    assert s.terms[0] == (3, 5)


def test_machins_formula():
    s = ArctanSum((16, sympy.Rational(1, 5)), (-4, sympy.Rational(1, 239)))
    assert isclose(float(s), pi)
