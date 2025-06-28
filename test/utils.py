def isclose(a, b, tol=1e-12):
    """Check if two values are close to each other."""
    return abs(a - b) < tol
