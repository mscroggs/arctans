"""Generate new formulae."""

import sympy
from arctans.arctans import Arctan, AbstractTerm
from arctans.reduction import reduce


def generate(
    known_formulae: list[AbstractTerm],
    *,
    max_denominator: int = 100,
    max_numerator: int = 1,
    max_terms: int | None = None,
    max_coefficient_denominator: int | None = None,
) -> list[AbstractTerm]:
    """Generate new formulae involving arctans."""
    value = float(known_formulae[0])
    for i in known_formulae[1:]:
        assert abs(float(i) - value) < 0.0001

    new_formulae = []
    for denominator in range(1, max_denominator + 1):
        for numerator in range(1, max_numerator + 1):
            a = Arctan(1, sympy.Rational(numerator, denominator))
            zero = reduce(a) - a
            for c, t in zero.terms:
                for f in known_formulae:
                    if t in f.term_dict:
                        new_f = f - zero * f.term_dict[t] / c
                        if new_f in known_formulae or new_f in new_formulae:
                            continue
                        if max_terms is not None and len(new_f.terms) >= max_terms:
                            continue
                        if (
                            max_coefficient_denominator is not None
                            and max(c.denominator for c, a in new_f.terms)
                            > max_coefficient_denominator
                        ):
                            continue
                        new_formulae.append(new_f)
    return new_formulae
