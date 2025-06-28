import pytest
from arctans import ArctanSum, irreducible, reduce
from utils import isclose

reducible = [3, 7, 8, 13, 17, 18, 21]


@pytest.mark.parametrize("n", [i for i in range(1, 23) if i not in reducible])
def test_irreducible(n):
    assert irreducible(n)


@pytest.mark.parametrize("n", reducible)
def test_reducible(n):
    assert not irreducible(n)


@pytest.mark.parametrize("n", reducible)
def test_reduction(n):
    arctan_n = ArctanSum((1, n))
    arctan_sum = reduce(arctan_n)
    assert isclose(float(arctan_n), float(arctan_sum))
    print(n)
    assert 1 == 0
