"""Functions for reducing arctans."""

import math as _math
import sympy
from arctans.primes import largest_pfactor, is_gaussian_prime, complex_factorise
from arctans.arctans import Arctan, Zero, AbstractTerm
from arctans.gaussian_integer import GaussianInteger


def irreducible(n: int) -> bool:
    """Check if arctan(n) is irreducible."""
    return largest_pfactor(1 + n**2) >= 2 * n


def convert_rational(arctan: AbstractTerm) -> AbstractTerm:
    """Convert a rational arccotan into a sum of integral arccotans."""
    assert arctan.nterms == 1
    if arctan.terms[0][1].numerator == 1:
        return arctan
    b = arctan.terms[0][1].numerator
    a = arctan.terms[0][1].denominator

    out = Zero()
    sign = 1
    while b > 0:
        n = a // b
        a, b = a * n + b, a % b
        out += Arctan(sign * arctan.terms[0][0], sympy.Rational(1, n))
        sign *= -1
    return out


def reduce(arctan: Arctan) -> AbstractTerm:
    """Reduce an arctan."""
    assert arctan.nterms == 1

    n = GaussianInteger(arctan.terms[0][1].denominator, arctan.terms[0][1].numerator)
    if is_gaussian_prime(n):
        return arctan

    out = Zero()
    for f in complex_factorise(n):
        out += convert_rational(Arctan(arctan.terms[0][0], sympy.Rational(f.imag, f.real)))

    c = int(_math.floor((float(arctan) - float(out)) * 4 / _math.pi + 0.1))
    out += Arctan(c, 1)
    return out
