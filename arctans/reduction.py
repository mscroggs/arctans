"""Functions for reducing arctans."""

from arctans.utils import largest_pfactor
from arctans.arctans import ArctanSum


def irreducible(n: int) -> bool:
    """Check if arctan(n) is irreducible."""
    return largest_pfactor(1 + n**2) >= 2 * n


def reduce(arctan: ArctanSum) -> ArctanSum:
    """Reduce an arctan."""
    assert arctan.nterms == 1
    raise NotImplementedError()
