"""Functions for reducing arctans."""

import sympy
from arctans.primes import largest_pfactor, is_gaussian_prime, complex_factorise, extract_real_imag
from arctans.arctans import ArctanSum


def irreducible(n: int) -> bool:
    """Check if arctan(n) is irreducible."""
    return largest_pfactor(1 + n**2) >= 2 * n


def convert_rational(arctan: ArctanSum) -> ArctanSum:
    """Convert a rational arccotan into a sum of integral arccotans."""
    assert arctan.nterms == 1
    if arctan.terms[0][1].denominator == 1:
        return arctan
    b = [arctan.terms[0][1].numerator]
    a = [arctan.terms[0][1].denominator]
    n = []

    while b[-1] > 0:
        n.append(a[-1] // b[-1])
        b.append(a[-1] % b[-1])
        a.append(a[-1] * n[-1] + b[-2])
    return ArctanSum(
        *[((-1) ** i * arctan.terms[0][0], sympy.Rational(1, j)) for i, j in enumerate(n)]
    )


def reduce(arctan: ArctanSum) -> ArctanSum:
    """Reduce an arctan."""
    assert arctan.nterms == 1

    complex = arctan.terms[0][1].denominator + 1j * arctan.terms[0][1].numerator
    if is_gaussian_prime(complex):
        return arctan

    fractions = []
    for f in complex_factorise(complex):
        real, imag = extract_real_imag(f)
        fractions.append((arctan.terms[0][0], sympy.Rational(imag, real)))
    return ArctanSum(*fractions)
