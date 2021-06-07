# JUST A COPY FROM Aufg.4!!!
# NOT FINISHED YET

class Produkt:

    MWST = 0.19
    ERM_MWST = 0.7

    def __init__(self, artikel_nr, bezeichnung, preis, isErmaessigt):
        self.__Artikel_Nr = artikel_nr
        self.__Bezeichnung = bezeichnung
        self.__PreisNetto = preis
        self.__Mehrwertsteuer = Produkt.ERM_MWST if (isErmaessigt) else Produkt.MWST

    def __str__(self):
        return 'Ich bin ein tolles Produkt'

    @property
    def Mehrwertsteuer(self):
        return self.__Mehrwertsteuer
    
    @property
    def Bruttopreis(self):
        return self.__PreisNetto + self.__PreisNetto * self.__Mehrwertsteuer

class Buch(Produkt):
    
    def __init__(self, artikel_nr, bezeichnung, preis, isErmaessigt, seitenzahl):
        super().__init__(artikel_nr, bezeichnung, preis, isErmaessigt)
        self.__Seitenzahl = seitenzahl

    def __str__(self):
        return 'Ich bin ein tolles Buch'

class DVD(Produkt):
    
    def __init__(self, artikel_nr, bezeichnung, preis, isErmaessigt, fsk):
        super().__init__(artikel_nr, bezeichnung, preis, isErmaessigt)
        self.__Fsk = fsk

    def __str__(self):
        return 'Ich bin eine tolle DVD'


class Warenkorb:
    
    def __init__(self):
        self.__Artikel = []

    def AddArtikel(self, object):
        self.__Artikel.append(object)
    
    def RemoveArtikel(self, object):
        self.__Artikel.remove(object)

    @property
    def Gesamtpreis(self):
        sum = 0
        for element in self.__Artikel:
            sum += element.Bruttopreis

        return sum


buch1 = Buch(1, 'Test1', 10.99, True, 345)
buch2 = Buch(1, 'Test2', 11.99, True, 456)

dvd1 = DVD(1, 'Test3', 12.99, False, 16)
dvd2 = DVD(1, 'Test4', 13.99, False, 18)

korb1 = Warenkorb()
korb1.AddArtikel(buch1)
korb1.AddArtikel(buch2)
korb1.AddArtikel(dvd1)
korb1.AddArtikel(dvd2)

print(korb1.Gesamtpreis)
