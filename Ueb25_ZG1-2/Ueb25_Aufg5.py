from tkinter import *

class Produkt:

    MWST = 0.19
    ERM_MWST = 0.7
    WAEHRUNG = '€'
    ZEILENUMBRUCH = '\n'
    PROZENT = '%'

    def __init__(self, artikel_nr, bezeichnung, preis, isErmaessigt):
        self.__Artikel_Nr = artikel_nr
        self.__Bezeichnung = bezeichnung
        self.__PreisNetto = preis
        self.__Mehrwertsteuer = Produkt.ERM_MWST if (isErmaessigt) else Produkt.MWST

    def __str__(self):
        rep = 'Artikelnr: ' + str(self.__Artikel_Nr) + Produkt.ZEILENUMBRUCH
        rep += 'Bezeichnung: ' + str(self.__Bezeichnung) + Produkt.ZEILENUMBRUCH
        rep += 'Preis (brutto): ' + str(self.Bruttopreis) + Produkt.WAEHRUNG + Produkt.ZEILENUMBRUCH
        rep += 'Mehrwertsteuer: ' + str(self.__Mehrwertsteuer * 100) + Produkt.PROZENT
        return rep

    @property
    def Artikelnr(self):
        return self.__Artikel_Nr

    @property
    def Bezeichnung(self):
        return self.__Bezeichnung
    
    @property
    def Bruttopreis(self):
        return round(self.__PreisNetto + self.__PreisNetto * self.__Mehrwertsteuer, 2)

class Buch(Produkt):
    
    def __init__(self, artikel_nr, bezeichnung, preis, isErmaessigt, seitenzahl):
        super().__init__(artikel_nr, bezeichnung, preis, isErmaessigt)
        self.__Seitenzahl = seitenzahl

    def __str__(self):
        rep =  'Buch:\n'
        rep += super().__str__() + super().ZEILENUMBRUCH
        rep += 'Seitenzahl: ' + str(self.__Seitenzahl)
        return rep

    @property
    def Artikelnr(self):
        return super().Artikelnr

    @property
    def Bezeichnung(self):
        return super().Bezeichnung
    
    @property
    def Bruttopreis(self):
        return super().Bruttopreis


class DVD(Produkt):

    def __init__(self, artikel_nr, bezeichnung, preis, isErmaessigt, fsk):
        super().__init__(artikel_nr, bezeichnung, preis, isErmaessigt)
        self.__Fsk = fsk

    def __str__(self):
        rep =  'DVD:\n'
        rep += super().__str__() + super().ZEILENUMBRUCH
        rep += 'FSK: ' + str(self.__Fsk)
        return rep

    @property
    def Artikelnr(self):
        return super().Artikelnr
    
    @property
    def Bezeichnung(self):
        return super().Bezeichnung

    @property
    def Bruttopreis(self):
        return super().Bruttopreis

class Warenkorb:
    
    def __init__(self):
        self.__Artikel = []

    def AddArtikel(self, object):
        self.__Artikel.append(object)
    
    def RemoveArtikel(self, object):
        self.__Artikel.remove(object)


    def __str__(self):

        def btn_berechne_gesamtsumme_click():
            sum = 0

            for element in self.__Artikel:

                sum += element.Bruttopreis
        
            lbl_unten.configure(text='Gesamtsumme der bestellten Artikel: ' + str(sum) + ' Euro')

        fenster = Tk()
        fenster.title('Warenkorb')

        lbl_oben = Label(fenster, text='Anzahl der bestellten Artikel: ' + str(len(self.__Artikel)))
        lbl_oben.pack()

        lbl_unten = Label(fenster, text='Gesamtsumme der bestellten Artikel: ??')
        lbl_unten.pack()

        btn_berechne_gesamtsumme = Button(fenster, text='Berechne Gesamtsumme', command=btn_berechne_gesamtsumme_click)
        btn_berechne_gesamtsumme.pack()

        fenster.mainloop()
    
    #------------------------------------------------------------------------------------------------------


buch1 = Buch(3445435, 'Test1', 10.99, True, 345)
buch2 = Buch(5686757, 'Test2', 11.99, True, 456)

dvd1 = DVD(456787, 'Test3', 12.99, False, 16)
dvd2 = DVD(453346, 'Test4', 13.99, False, 18)

korb1 = Warenkorb()
korb1.AddArtikel(buch1)
korb1.AddArtikel(buch2)
korb1.AddArtikel(dvd1)
korb1.AddArtikel(dvd2)

print(korb1)