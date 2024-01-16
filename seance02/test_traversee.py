"""Description.

Tests de la librairie lib_traversee.py
"""
from lib_traversee import (
    _etats,
    verifie_contraintes,
    Etat,
    Rive,
    sont_connectes,
)


def test_construction_etats():
    """Tests empiriques

    Il doit y avoir 16 etats sans duplication!
    """
    assert len(_etats) == 16
    assert len(set(_etats)) == 16


def test_verifie_contraintes():
    """Test positif et négatif pour chaque contrainte"""
    positif = Etat(
        berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
    )
    assert verifie_contraintes(positif)
    negatif_loup_mouton = Etat(
        berger=Rive.GAUCHE, loup=Rive.DROITE, mouton=Rive.DROITE, chou=Rive.GAUCHE
    )
    assert not verifie_contraintes(negatif_loup_mouton)
    negatif_mouton_chou = Etat(
        berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.DROITE, chou=Rive.DROITE
    )
    assert not verifie_contraintes(negatif_mouton_chou)


def test_sont_connectes_positif():
    """Vérifie que la détection des connections fonctionne

    berger traverse seul
    berger loup traversent
    berger mouton traversent
    berger chou traversent
    """
    assert sont_connectes(
        etat1=Etat(
            berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
        etat2=Etat(
            berger=Rive.DROITE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
    )
    assert sont_connectes(
        etat1=Etat(
            berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
        etat2=Etat(
            berger=Rive.DROITE, loup=Rive.DROITE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
    )
    assert sont_connectes(
        etat1=Etat(
            berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
        etat2=Etat(
            berger=Rive.DROITE, loup=Rive.GAUCHE, mouton=Rive.DROITE, chou=Rive.GAUCHE
        ),
    )
    assert sont_connectes(
        etat1=Etat(
            berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
        etat2=Etat(
            berger=Rive.DROITE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.DROITE
        ),
    )


def test_sont_connectes_negatif():
    """Vérifie que la détection des connections fonctionne

    2 taversent dont le berger mais pas dans le même sens
    2 traversent mais pas le berger
    3 traversent dans le bon sens avec le berger
    """
    assert not sont_connectes(
        etat1=Etat(
            berger=Rive.GAUCHE, loup=Rive.DROITE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
        etat2=Etat(
            berger=Rive.DROITE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
    )
    assert not sont_connectes(
        etat1=Etat(
            berger=Rive.GAUCHE, loup=Rive.DROITE, mouton=Rive.GAUCHE, chou=Rive.DROITE
        ),
        etat2=Etat(
            berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
        ),
    )
    assert not sont_connectes(
        etat1=Etat(
            berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.DROITE
        ),
        etat2=Etat(
            berger=Rive.DROITE, loup=Rive.DROITE, mouton=Rive.DROITE, chou=Rive.GAUCHE
        ),
    )
