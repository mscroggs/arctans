from arctans import ArctanSum


def test_simplify():
    s = ArctanSum((1, 5), (2, 5))
    assert s.nterms == 1
    assert s.terms[0] == (3, 5)
