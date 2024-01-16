"""Description.

Librairie permettant de modéliser le problème de traversée de rivière en terme de Graphe.
"""
from enum import Enum
from dataclasses import dataclass


class Rive(Enum):
    """Représente les deux côté possibles de la rivière""" 
    GAUCHE = "gauche"
    DROITE = "droite"


@dataclass(frozen=True, unsafe_hash=True)
class Etat:
    """Représente un état entre deux traversées de barque
    
    Ne prend pas en compte les contraintes supplémentaires du problème.
    """
    berger: Rive
    loup: Rive
    mouton: Rive
    chou: Rive


# les constantes sont par convention toute en majuscule
DEPART: Etat = Etat(
    berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
)

ARRIVEE: Etat = Etat(
    berger=Rive.DROITE, loup=Rive.DROITE, mouton=Rive.DROITE, chou=Rive.DROITE
)

# les variables "privées" sont par convention précédées d'un _ (underscore)
_etats: list[Etat] = list()
for berger in Rive:
    for loup in Rive:
        for mouton in Rive:
            for chou in Rive:
                _etats.append(
                    Etat(
                        berger=berger,
                        loup=loup,
                        mouton=mouton,
                        chou=chou,
                    )
                )


def verifie_contraintes(etat: Etat) -> bool:
    """Verifie si les contraintes loup/mouton mouton/chou sont respectees
    
    Exemples:
    >>> positif = Etat(
    ...         berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, chou=Rive.GAUCHE
    ...     )
    >>> verifie_contraintes(positif)
    True
    >>> negatif_loup_mouton = Etat(
    ...         berger=Rive.GAUCHE, loup=Rive.DROITE, mouton=Rive.DROITE, chou=Rive.GAUCHE
    ...     )
    >>> verifie_contraintes(negatif_loup_mouton)
    False
    >>> negatif_mouton_chou = Etat(
    ...         berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.DROITE, chou=Rive.DROITE
    ...     )
    >>> verifie_contraintes(negatif_mouton_chou)
    False
    """
    if etat.loup == etat.mouton and etat.berger != etat.loup:
        return False
    if etat.mouton == etat.chou and etat.berger != etat.mouton:
        return False
    return True


SOMMETS: list[Etat] = [etat for etat in _etats if verifie_contraintes(etat)]


def sont_connectes(etat1: Etat, etat2: Etat) -> bool:
    """Vérifie que les etats sont connectes par une traversée de barque"""
    if etat1.berger == etat2.berger:
        return False
    nombre_de_changement = 0
    if etat1.mouton != etat2.mouton:
        nombre_de_changement += 1
        if etat1.mouton != etat1.berger:
            return False
    if etat1.loup != etat2.loup:
        nombre_de_changement += 1
        if etat1.loup != etat1.berger:
            return False
    if etat1.chou != etat2.chou:
        nombre_de_changement += 1
        if etat1.chou != etat1.berger:
            return False
    return nombre_de_changement <= 1


ARRETES: list[tuple[Etat, Etat]] = [
    (sommet1, sommet2)
    for sommet1 in SOMMETS
    for sommet2 in SOMMETS
    if sont_connectes(sommet1, sommet2)
]
