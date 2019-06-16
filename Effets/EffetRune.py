from Effets.Effet import Effet
import Niveau

class EffetRune(Effet):
    """@summary: Classe décrivant un effet de sort. Les sorts sont découpés en 1 ou + effets.
    Cet effet pose une rune sur la grille de jeu."""

    def __init__(self, duree, list_effets, str_nom, tuple_couleur, **kwargs):
        """@summary: Initialise un effet posant une rune.
        @duree: Le nombrede tour où la rune sera présente (avant déclenchement)
        @type: int
        @sort_sort: le sort lancé sur la case centrale du piège
        @type: Sort
        @str_nom: le nom de la rune
        @type: string
        @tuple_couleur: la couleur du piège
        @type: tuple de couleur format RGB
        @kwargs: Options de l'effets
        @type: **kwargs"""
        self.kwargs = kwargs
        self.duree = duree
        self.effets = list_effets
        self.nom = str_nom
        self.couleur = tuple_couleur
        super(EffetRune, self).__init__(**kwargs)

    def deepcopy(self):
        return EffetRune(self.duree, self.effets, self.nom, self.couleur, **self.kwargs)

    def appliquerEffet(self, niveau, joueurCaseEffet, joueurLanceur, **kwargs):
        """@summary: Appelé lors de l'application de l'effet.
        @niveau: la grille de simulation de combat
        @type: Niveau
        @joueurCaseEffet: le joueur se tenant sur la case dans la zone d'effet
        @type: Personnage
        @joueurLanceur: le joueur lançant l'effet
        @type: Personnage
        @kwargs: options supplémentaires, case_cible_x et case_cible_y doivent être mentionés
        @type: **kwargs"""
        nouvelleRune = Niveau.Rune(self.nom, self.duree, self.effets, kwargs.get(
            "case_cible_x"), kwargs.get("case_cible_y"), joueurLanceur, self.couleur)
        niveau.poseRune(nouvelleRune)
