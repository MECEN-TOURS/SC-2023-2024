"""Description.

Tests pour le parcours de graphe.
"""
from lib_graphe import sont_relies, trouve_chemin, remonte_arbre, trouve_chemins
import pytest

@pytest.fixture
def exemple_arretes():
    return [
        tuple("AB"),
        tuple("AC"),
        tuple("BD"),
        tuple("CB"),
        tuple("CD"),
        tuple("DE"),
        tuple("EF"),
        tuple("FD"),
        tuple("FC"),
    ]


def test_sont_relies_long():
    """Long graphe linéaire pour vérifier qu'il n'y a pas de RecursionError"""
    nb_sommets = 2000
    arretes = [(str(i), str(i+1)) for i in range(nb_sommets)]
    assert sont_relies(depart=str(0), arrivee=str(nb_sommets), arretes=arretes)


def test_sont_relies(exemple_arretes):
    """Test positif et négatif"""
    assert sont_relies(depart="A", arrivee="B", arretes=exemple_arretes)
    assert sont_relies(depart="A", arrivee="F", arretes=exemple_arretes)
    assert not sont_relies(depart="B", arrivee="A", arretes=exemple_arretes)


def test_remonte_arbre():
    arbre = dict(B="A", C="A", D="B", E="D", F="E")
    assert remonte_arbre(depart="A", arrivee="F", arbre=arbre) == ["A", "B", "D", "E", "F"]

def test_trouve_chemin_long():
    """Long graphe linéaire pour vérifier qu'il n'y a pas de RecursionError"""
    nb_sommets = 2000
    arretes = [(str(i), str(i+1)) for i in range(nb_sommets)]
    resultat = trouve_chemin(depart=str(0), arrivee=str(nb_sommets), arretes=arretes)
    attendu = [str(i) for i in range(nb_sommets + 1)]
    assert resultat == attendu

def test_trouve_chemin(exemple_arretes):
    """Teste deux exemples de chemins"""
    assert trouve_chemin(depart="A", arrivee="B", arretes=exemple_arretes) == ["A", "B"]
    assert trouve_chemin(depart="A", arrivee="F", arretes=exemple_arretes) == ["A", "B", "D", "E", "F"]

def test_trouve_chemin_plantage(exemple_arretes):
    """Teste le plantage en cas d'absence de chemin"""
    with pytest.raises(ValueError):
        trouve_chemin(depart="B", arrivee="A", arretes=exemple_arretes)


def test_trouve_chemins(exemple_arretes):
    assert trouve_chemins(depart="A", arrivee="B", arretes=exemple_arretes) == [
        list("AB"),
        list("ACB"),

    ]
    assert trouve_chemins(depart="B", arrivee="A", arretes=exemple_arretes) == []