from math import pi
import pytest
from arctans import Arctan, generate
from utils import isclose


@pytest.mark.parametrize("max_a", [10, 25])
def test(max_a):
    formulae = generate([Arctan(4, 1)], max_a, 8)
    for f in formulae:
        assert isclose(float(f), pi)
