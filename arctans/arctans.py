class ArctanSum:
    """The sum of some arctans."""

    def __init__(self, *terms: tuple[int, int]):
        self._terms = terms

    def nterms(self):
        return len(self._terms)
