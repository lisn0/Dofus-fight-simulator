"""@summary: Rassemble les sorts de l'éniripsa
"""
# pylint: disable=line-too-long
import Sort
from Effets.EffetDegats import EffetDegats
from Effets.EffetSoin import EffetSoinSelonSubit, EffetSoin
from Effets.EffetEtat import EffetEtat, EffetRetireEtat
from Effets.EffetGlyphe import EffetGlyphe
from Etats.EtatEffet import EtatEffetSiSubit, EtatEffetFinTour
import Zones

import Personnages


def getSortsDebutCombat(lvl):
    """@summary: charge les sorts de début de combat
    @return: List <Sort>
    """
    # pylint: disable=unused-argument
    sortsDebutCombat = []
    return sortsDebutCombat


def getSorts(lvl):
    """@summary: charge les sorts de combat
    @return: List <Sort>
    """
    sorts = []
    motDAirEffetAvant = EffetEtat(EtatEffetSiSubit('Etat temporaire', 0, 1, EffetSoinSelonSubit(
        100, zone=Zones.TypeZoneCercleSansCentre(2), cibles_possibles="Allies"), "Mots d'Air", "lanceur", "attaquant"))
    motDAirEffetApres = EffetRetireEtat('Etat temporaire')
    sorts.append(Personnages.Personnage.getSortRightLvl(lvl, [
        Sort.Sort("Mot Blessant", 1, 4, 1, 6, [motDAirEffetAvant, EffetDegats(13, 15, "Air"), motDAirEffetApres], [motDAirEffetAvant, EffetDegats(17, 17, "Air"), motDAirEffetApres], 15, 3, 2, 0, 1, "cercle", True, description="""Occasionne des dommages Air.
        Les alliés à proximité du lanceur (2 cases ou moins) sont soignés à hauteur de 100% des dommages occasionnés.""", chaine=True),

        Sort.Sort("Mot Blessant", 30, 4, 1, 7, [motDAirEffetAvant, EffetDegats(16, 18, "Air"), motDAirEffetApres], [motDAirEffetAvant, EffetDegats(20, 20, "Air"), motDAirEffetApres], 15, 3, 2, 0, 1, "cercle", True, description="""Occasionne des dommages Air.
        Les alliés à proximité du lanceur (2 cases ou moins) sont soignés à hauteur de 100% des dommages occasionnés.""", chaine=True),

        Sort.Sort("Mot Blessant", 60, 4, 1, 8, [motDAirEffetAvant, EffetDegats(19, 21, "Air"), motDAirEffetApres], [motDAirEffetAvant, EffetDegats(23, 23, "Air"), motDAirEffetApres], 15, 3, 2, 0, 1, "cercle", True, description="""Occasionne des dommages Air.
        Les alliés à proximité du lanceur (2 cases ou moins) sont soignés à hauteur de 100% des dommages occasionnés.""", chaine=True)
    ]))
    sorts.append(Personnages.Personnage.getSortRightLvl(lvl, [
        Sort.Sort("Mot Vexant", 110, 5, 1, 5, [EffetDegats(48, 52, "Air")], [EffetDegats(58, 62, "Air")], 5, 2, 1, 0, 0, "ligne", True, description="""Occasionne des dommages Air.""", chaine=True)
    ]))
    sorts.append(Personnages.Personnage.getSortRightLvl(lvl, [
        Sort.Sort("Mot Alternatif", 1, 3, 1, 4, [EffetSoin(14, 17, cibles_possibles="Allies"), EffetDegats(10, 13, "Feu", cibles_possibles="Ennemis")], [EffetSoin(18, 18, cibles_possibles="Allies"), EffetDegats(13, 13, "Feu", cibles_possibles="Ennemis")], 5, 3, 2, 0, 1, "cercle", True, description="""Occasionne des dommages Feu aux ennemis.
    Soigne les alliés.""", chaine=False),

        Sort.Sort("Mot Alternatif", 20, 3, 1, 6, [EffetSoin(19, 22, cibles_possibles="Allies"), EffetDegats(13, 16, "Feu", cibles_possibles="Ennemis")], [EffetSoin(23, 23, cibles_possibles="Allies"), EffetDegats(17, 17, "Feu", cibles_possibles="Ennemis")], 5, 3, 2, 0, 1, "cercle", True, description="""Occasionne des dommages Feu aux ennemis.
    Soigne les alliés.""", chaine=False),

        Sort.Sort("Mot Alternatif", 40, 3, 1, 8, [EffetSoin(24, 27, cibles_possibles="Allies"), EffetDegats(16, 19, "Feu", cibles_possibles="Ennemis")], [EffetSoin(28, 28, cibles_possibles="Allies"), EffetDegats(21, 21, "Feu", cibles_possibles="Ennemis")], 5, 3, 2, 0, 1, "cercle", True, description="""Occasionne des dommages Feu aux ennemis.
    Soigne les alliés.""", chaine=False)
    ]))
    activationMotMarquant = Sort.Sort("Glyphe Marquant", 0, 0, 0, 2, [EffetEtat(EtatEffetFinTour("Glyphe Marquant", 0, 1, EffetSoin(1, 1), "Glyphe Marquant", "lanceur"), cibles_possibles="Allies")], [], 0, 99, 99, 0, 0, "cercle", False)
    sortieMotMarquant = Sort.Sort("Sortie Glyphe Marquant", 0, 0, 0, 3, [EffetRetireEtat("Glyphe Marquant")], [], 0, 99, 99, 0, 0, "cercle", False)
    sorts.append(Personnages.Personnage.getSortRightLvl(lvl, [
        Sort.Sort("Mot Marquant", 101, 4, 1, 5, [EffetGlyphe(activationMotMarquant, activationMotMarquant, sortieMotMarquant, 1, "Mot Marquant", (252, 116, 172), zone=Zones.TypeZoneCercle(2), cibles_possibles="Ennemis"), EffetDegats(30, 34, "Feu")], [EffetGlyphe(activationMotMarquant, activationMotMarquant, sortieMotMarquant, 1, "Mot Marquant", (252, 116, 172), zone=Zones.TypeZoneCercle(2), cibles_possibles="Ennemis"), EffetDegats(33, 37, "Feu")], 25, 3, 2, 0, 0, "cercle", True, description="""Occasionne des dommages Feu.
    Pose un glyphe autour de la cible ennemie. Le glyphe soigne les alliés en fin de tour.""", chaine=True)
    ]))
    return sorts
