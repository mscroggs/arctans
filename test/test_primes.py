import pytest
from todd import largest_pfactor

primes = [2]
for i in range(3, 1000, 2):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)



@pytest.mark.parametrize("n", range(2, 1000))
def test_largest_pfactor(n):
    assert largest_pfactor(n) == max(p for p in primes if n % p == 0)
