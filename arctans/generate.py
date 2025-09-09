"""Generate new formulae."""

import sympy
from arctans.arctans import Arctan, AbstractTerm
from arctans import reduce


def generate(
    known_formulae: list[AbstractTerm],
    max_a: int = 100,
    max_terms: int | None = None,
) -> list[AbstractTerm]:
    """Generate new formulae involving arctans."""
    value = float(known_formulae[0])
    for i in known_formulae[1:]:
        assert abs(float(i) - value) < 0.0001

    formulae = [i for i in known_formulae]

    for i in range(1, max_a + 1):
        a = Arctan(1, sympy.Rational(1, i))
        zero = reduce(a) - a
        for c, t in zero.terms:
            for f in formulae:
                if t in f.term_dict:
                    new_f = f - zero * f.term_dict[t] / c
                    if new_f in formulae:
                        continue
                    if max_terms is not None and len(new_f.terms) >= max_terms:
                        continue
                    formulae.append(new_f)
    return formulae
