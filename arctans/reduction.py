"""Functions for reducing arctans."""

import math as _math
from arctans.primes import is_gaussian_prime, complex_factorise
from arctans.arctans import arccotan, arctan, Zero, AbstractTerm, Arctan
from arctans.numbers import Rational, GaussianInteger


def convert_rational_single_arctan(a: Arctan) -> AbstractTerm:
    """Convert a rational arccotangent into a sum of integral arccotangents.

    Args:
        a: An arctan

    Returns:
        A sum of integral arccotangents
    """
    if a.terms[0][1].numerator == 1:
        return a
    beta = a.terms[0][1].numerator
    alpha = a.terms[0][1].denominator

    out = Zero()
    sign = 1
    while beta > 0:
        n = alpha // beta
        alpha, beta = alpha * n + beta, alpha % beta
        assert isinstance(a.terms[0][0] * arccotan(n), AbstractTerm)
        out += sign * a.terms[0][0] * arccotan(n)
        sign *= -1
    return out


def convert_rational(a: AbstractTerm) -> AbstractTerm:
    """Convert a rational arccotangent into a sum of integral arccotangents.

    Args:
        a: An arctan or sum of arctans

    Returns:
        A sum of integral arccotangents
    """
    if isinstance(a, Arctan):
        return convert_rational_single_arctan(a)
    out = Zero()
    for i, j in a.terms:
        out += i * convert_rational_single_arctan(arctan(j))
    return out


def reduce_single_arctan(a: Arctan) -> AbstractTerm:
    """Express an arctan as a sum of irreducible integral arccotangents.

    Args:
        a: An arctan

    Returns:
        A sum of irreducible integral arccotangents
    """
    n = GaussianInteger(a.terms[0][1].denominator, a.terms[0][1].numerator)
    if is_gaussian_prime(n):
        return a

    out = Zero()
    for f in complex_factorise(n):
        out += a.terms[0][0] * convert_rational(arctan(Rational(int(f.imag), int(f.real))))

    c = int(_math.floor((float(a) - float(out)) * 4 / _math.pi + 0.1))
    out += c * arctan(1)
    return out


def reduce(a: AbstractTerm) -> AbstractTerm:
    """Express an arctan as a sum of irreducible integral arccotangents.

    Args:
        a: An arctan or sum of arctans

    Returns:
        A sum of irreducible integral arccotangents
    """
    if isinstance(a, Arctan):
        return reduce_single_arctan(a)

    out = Zero()
    for i, j in a.terms:
        out += i * reduce_single_arctan(arctan(j))
    return out
