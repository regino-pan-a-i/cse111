from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full():
    assert make_full_name ("Andre", "Regino") == "Regino; Andre"
    assert make_full_name ("Julio", "Paniagua") == "Paniagua; Julio"
    assert make_full_name ("Adriana", "Díaz") == "Díaz; Adriana"
    assert make_full_name ("Carlos", "Regino") == "Regino; Carlos"
    assert make_full_name ("Cesar", "Ventura") == "Ventura; Cesar"


def test_extract_family_name():
    assert extract_family_name ("Regino; Andre") == "Regino"
    assert extract_family_name ("Paniagua; Julio") == "Paniagua"
    assert extract_family_name ("Díaz; Maricela") == "Díaz"
    assert extract_family_name ("Regino; Carlos") == "Regino"
    assert extract_family_name ("Ventura; Cesar") == "Ventura"

def test_extract_given_name():
    assert extract_given_name ("Regino; Andre") == "Andre"
    assert extract_given_name ("Paniagua; Julio") == "Julio"
    assert extract_given_name ("Díaz; Maricela") == "Maricela"
    assert extract_given_name ("Regino; Carlos") == "Carlos"
    assert extract_given_name ("Ventura; Cesar") == "Cesar"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
