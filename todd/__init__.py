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
