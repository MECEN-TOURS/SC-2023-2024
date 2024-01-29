"""Description.

Librairie de parcours de graphe
"""
from collections import deque


def sont_relies(depart: str, arrivee: str, arretes: list[tuple[str, str]]) -> bool:
    vus, visites = list(), list()
    vus.append(depart)
    while vus:
        sommet_courant = vus.pop()
        visites.append(sommet_courant)
        if sommet_courant == arrivee:
            return True
        voisins = [n2 for (n1, n2) in arretes if n1 == sommet_courant]
        for voisin in voisins:
            if voisin not in visites:
                vus.append(voisin)
    return False
        
def remonte_arbre(depart: str, arrivee: str, arbre: dict[str, str]) -> list[str]:
    chemin = [arrivee]
    while chemin[-1] in arbre:
        chemin.append(arbre[chemin[-1]])
    if chemin[-1] == depart:
        return list(reversed(chemin))
    else:
        raise ValueError("Les sommets ne sont pas reliés!")

def trouve_chemin(depart: str, arrivee: str, arretes: list[tuple[str, str]]) -> list[str]:
    """Renvoie un chemin reliant depart à arrivee
    
    Souleve une exception s'il n'y a pas de chemin"""
    vus, visites, arbre = deque(), set(), dict()
    vus.append(depart)
    while vus:
        sommet_courant = vus.pop()
        if sommet_courant in visites:
            continue
        visites.add(sommet_courant)
        if sommet_courant == arrivee:
            break
        voisins = [n2 for (n1, n2) in arretes if n1 == sommet_courant]
        for voisin in voisins:
            if voisin not in visites:
                vus.appendleft(voisin)
                if voisin not in arbre:
                    arbre[voisin] = sommet_courant
    #breakpoint()
    return remonte_arbre(depart=depart, arrivee=arrivee, arbre=arbre)


def trouve_chemins(depart: str, arrivee: str, arretes: list[tuple[str, str]]) -> list[list[str]]:
    if depart == arrivee:
        return [[depart]]
    voisins = [n2 for (n1, n2) in arretes if n1 == depart]
    resultat = list()
    sous_graphe = [(n1, n2) for (n1, n2) in arretes if n1 != depart and n2 != depart]
    for voisin in voisins:
        for chemin in trouve_chemins(
                depart=voisin, 
                arrivee=arrivee, 
                arretes=sous_graphe
            ):
            resultat.append([depart] + chemin)
    return resultat
    
        
