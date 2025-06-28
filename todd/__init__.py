def largest_pfactor(n: int) -> int:
    """Compute the largest prime factor of n."""
    i = 1
    while i < n:
        i += 1
        while i < n and n % i == 0:
            n //= i
    return n
