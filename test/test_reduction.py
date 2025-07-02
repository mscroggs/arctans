import pytest
import sympy
from arctans import ArctanSum, is_irreducible, reduce, convert_rational
from utils import isclose

reducible = [3, 7, 8, 13, 17, 18, 21]


@pytest.mark.parametrize("n", range(1, 23))
def test_irreducible(n):
    assert is_irreducible(n) == (n not in reducible)


@pytest.mark.parametrize("numerator", range(1, 20))
@pytest.mark.parametrize("denominator", range(1, 20))
def test_convert_rational(numerator, denominator):
    arctan_n = ArctanSum((numerator, denominator))
    arctan_sum = convert_rational(arctan_n)
    assert isclose(float(arctan_n), float(arctan_sum))
    for i, j in arctan_sum.terms:
        assert j.denominator == 1


@pytest.mark.parametrize("n", reducible)
@pytest.mark.parametrize("c", [-2, -1, 1, 3, sympy.Rational(1, 2)])
def test_reduction(c, n):
    arctan_n = ArctanSum((c, n))
    arctan_sum = reduce(arctan_n)
    assert isclose(float(arctan_n), float(arctan_sum))
    assert arctan_sum.nterms > 1
