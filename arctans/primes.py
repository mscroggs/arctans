"""Mathematical utility functions."""

from functools import cache

primes = [2]


def largest_pfactor(n: int) -> int:
    """Compute the largest prime factor of n."""
    if n < 2:
        raise ValueError(f"Cannot find largest prime factor of {n}")
    i = 2
    while i < n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n


def is_prime(n: int) -> bool:
    """Check if an integer is prime."""
    global primes

    i = primes[-1]
    while primes[-1] < n:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 1
    return n in primes


def irreducible(n: int) -> bool:
    """Check if arctan(n) is irreducible."""
    return largest_pfactor(1 + n**2) >= 2 * n


def is_gaussian_prime(n: complex) -> bool:
    """Check if n is a Gaussian prime."""
    assert is_gaussian_integer(n)
    if n.real > 0:
        real = int(n.real + 0.1)
    else:
        real = int(n.real - 0.1)
    if n.imag > 0:
        imag = int(n.imag + 0.1)
    else:
        imag = int(n.imag - 0.1)
    if imag == 0 or real == 0:
        k = abs(real) + abs(imag)
        return k % 4 == 3 and is_prime(k)
    return is_prime(real**2 + imag**2)


def is_gaussian_unit(n: complex) -> bool:
    """Check if n is a Gaussian unit."""
    assert is_gaussian_integer(n)
    if n.real > 0:
        real = int(n.real + 0.1)
    else:
        real = int(n.real - 0.1)
    if n.imag > 0:
        imag = int(n.imag + 0.1)
    else:
        imag = int(n.imag - 0.1)
    return abs(real) + abs(imag) <= 1


def is_gaussian_integer(n: complex) -> bool:
    """Check if n is a Gaussian integer."""
    if n.real > 0:
        real = int(n.real + 0.1)
    else:
        real = int(n.real - 0.1)
    if n.imag > 0:
        imag = int(n.imag + 0.1)
    else:
        imag = int(n.imag - 0.1)
    return abs(n - real - 1j * imag) < 1e-10


@cache
def complex_factorise(n: complex) -> list[complex]:
    """Factorise a Gaussian integer into Gaussian primes."""
    if is_gaussian_unit(n) or is_gaussian_prime(n):
        return [n]
    lim = int(abs(n)) + 1
    for i in range(lim + 1):
        for j in range(-lim, lim + 1):
            if abs(i) + abs(j) <= 1:
                continue
            if not is_gaussian_integer(i + j * 1j):
                continue
            m = i + j * 1j
            d = n / m
            if abs(d) > 1:
                continue
            if is_gaussian_integer(d):
                return [m] + complex_factorise(d)
    raise RuntimeError(f"Could not fund factor of non-prime number: {n}")
