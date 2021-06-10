class Produkt:

    WAEHRUNG = '€'
    ZEILENUMBRUCH = '\n'
    PROZENT = '%'

    def __init__(self, artikel_nr, bezeichnung, preis):
        self.__Artikel_Nr = artikel_nr
        self.__Bezeichnung = bezeichnung
        self.__PreisNetto = preis

    def __str__(self):
        rep = 'Artikelnr: ' + str(self.__Artikel_Nr) + Produkt.ZEILENUMBRUCH
        rep += 'Bezeichnung: ' + str(self.__Bezeichnung) + Produkt.ZEILENUMBRUCH
        rep += 'Preis (brutto): ' + str(self.Bruttopreis) + Produkt.WAEHRUNG + Produkt.ZEILENUMBRUCH
        return rep

    @property
    def Artikelnr(self):
        return self.__Artikel_Nr
    
    @property
    def Nettopreis(self):
        return self.__PreisNetto

    @property
    def Bezeichnung(self):
        return self.__Bezeichnung

class Buch(Produkt):

    MWST = 0.7
    
    def __init__(self, artikel_nr, bezeichnung, preis, seitenzahl):
        super().__init__(artikel_nr, bezeichnung, preis)
        self.__Seitenzahl = seitenzahl

    def __str__(self):
        rep = 'Buch - ' + self.Bezeichnung + ' (Art.-Nr: '  + str(self.Artikelnr) + ')\t' + str(self.Bruttopreis) + ' Euro'
        return rep

    @property
    def Artikelnr(self):
        return super().Artikelnr

    @property
    def Bezeichnung(self):
        return super().Bezeichnung

    @property
    def Nettopreis(self):
        return super().Nettopreis
    
    @property
    def Bruttopreis(self):
        return round(self.Nettopreis + self.Nettopreis * Buch.MWST, 2)
        

class DVD(Produkt):

    MWST = 0.19

    def __init__(self, artikel_nr, bezeichnung, preis, fsk):
        super().__init__(artikel_nr, bezeichnung, preis)
        self.__Fsk = fsk

    def __str__Alt(self):
        rep =  'DVD:\n'
        rep += super().__str__()
        rep += 'FSK: ' + str(self.__Fsk)
        return rep


    def __str__(self):
        rep = 'DVD - ' + self.Bezeichnung + ' (Art.-Nr: '  + str(self.Artikelnr) + ')\t' + str(self.Bruttopreis) + ' Euro'
        return rep
        

    @property
    def Artikelnr(self):
        return super().Artikelnr
    
    @property
    def Bezeichnung(self):
        return super().Bezeichnung

    @property
    def Nettopreis(self):
        return super().Nettopreis
    
    @property
    def Bruttopreis(self):
        return round(self.Nettopreis + self.Nettopreis * DVD.MWST, 2)

class Warenkorb:
    
    def __init__(self):
        self.__Artikel = []

    def AddArtikel(self, object):
        self.__Artikel.append(object)
    
    def RemoveArtikel(self, object):
        self.__Artikel.remove(object)

    def __str__(self):

        rep =  ''
        sum = 0

        for element in self.__Artikel:

            sum += element.Bruttopreis
            
            rep += str(element)
            rep += '\n'
        
        rep += '-----------------------------------------------\n'
        rep += 'Gesamtpreis: ' + str(sum) + ' Euro'

        return rep
    
    #------------------------------------------------------------------------------------------------------


buch1 = Buch(3445435, 'Test1', 10.99, 345)
buch2 = Buch(5686757, 'Test2', 11.99, 456)

dvd1 = DVD(456787, 'Test3', 12.99, 16)
dvd2 = DVD(453346, 'Test4', 13.99, 18)

print(dvd1)

korb1 = Warenkorb()

korb1.AddArtikel(buch1)
korb1.AddArtikel(buch2)
korb1.AddArtikel(dvd1)
korb1.AddArtikel(dvd2)

print('\n')

print(korb1)