# tests/test_basic.py

from aganitha_papers.get_papers.filter import is_non_academic


def test_is_non_academic_positive():
    assert is_non_academic("XYZ Therapeutics Inc, USA")


def test_is_non_academic_negative():
    assert not is_non_academic("Harvard University, Boston")


def test_is_non_academic_edge_case():
    assert not is_non_academic("University Hospital, Pharma Department")


def test_company_affiliation_detected():
    assert is_non_academic("Moderna Inc., Cambridge, MA")


def test_academic_affiliation_skipped():
    assert not is_non_academic("Harvard University, Department of Biology")

####    to run test give command 
#       poetry run pytest