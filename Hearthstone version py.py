
    

from doctest import REPORT_CDIFF


class Carte:
    def __init__(self, nom, mana, description):
        self.nom = nom
        self.mana = mana
        self.description = description
    
    def getnom(self):
        return self.nom

    def getmana(self):
        return self.mana

    def getdescription(self):
        return self.description


class Mage:
    def __init__(self, nom, PV, Valeurmana, Total):
        self.nom = nom
        self.PV = PV
        self.Valeurmana = Valeurmana
        self.Total = Total

    def getnom(self):
        return self.nom

    def getPV(self):
        return self.PV

    def getValeurmana(self):
        return self.Valeurmana

    def getTotal(self):
        return self.Total

class Cristal:
    def __init__(self, valeurs, coutmana):
        self.valeurs = valeurs
        self.coutmana = coutmana

    def getvaleurs(self):
        return self.valeurs

    def getcoutmana(self):
        return self.coutmana

class Créature:
    def __init__(self, PV, scoreatk, coutmana, mort, perdPV):
        self.PV = PV
        self.scoreatk = scoreatk
        self.coutmana = coutmana
        self.mort = mort
        self.perdPV = perdPV

    def getPV(self):
        return self.PV

    def getscoreatk(self):
        return self.scoreatk

    def getcoutmana(self):
        return self.coutmana

    def getmort(self):
        return self.mort

    def getperdPV(self):
        return self.perdPV

class Blast:
    def __init__(self, valeur, perdPV):
        self.valeur = valeur
        self.perdPV = perdPV

    def getvaleur(self):
        return self.valeur

    def getperdPV(self):
        return self.perdPV

class joueur:
    def __init__(self, Nom, Pointdevie, Mana, Total, hp, atk):
        self.Nom = Nom
        self.Pointdevie = Pointdevie
        self.Mana = Mana
        self.Total = Total

    def getNom(self):
        return self.Nom

    def getPointdevie(self):
        return self.Pointdevie

    def getMana(self):
        return self.Mana

    def getTotal(self):
        return self.Total

    def gethp(self):
        return self.hp

    def getatk(self):
        return self.atk

def __init__(self, hp, atk):
        self.hp = 100
        self.atk = 4
        
def perdPv(self):
        self.hp = self.hp - self.atk

def afficheVie(self):
        return self.hp

joueur1 = joueur("Mage Albert")

joueur1.perdPv()
print(joueur1.afficheVie())