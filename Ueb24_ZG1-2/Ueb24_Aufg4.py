from tkinter import *
from mein_paket import funkt as mad

 # Erzeugen vom MainWindow
mainform = Tk()
mainform.title('Blubb')
mainform.geometry("250x140")

 # Erzeugen von syst. Label sowie Textfeld
lbl_sys = Label(mainform, text="Systolischer Blutdruck")
lbl_sys.pack()
txt_sys = Entry(mainform)
txt_sys.pack()

 # Erzeugen von Diast. Label sowie Textfeld
lbl_dia = Label(mainform, text="Diast. Blutdruck")
lbl_dia.pack()
txt_dia = Entry(mainform)
txt_dia.pack()

 # Ergebnis Label
lbl_mad = Label(text="MAD: ?")
lbl_mad.pack()

 # Funktionsdefinition für ClickEvent
def btn_berechne_click():
    sys = float(txt_sys.get())
    dias = float(txt_dia.get())
    lbl_mad["text"] = "MAD: " + str(mad.mad_berechnen(sys, dias))

 # Erzeugung des Buttons und zuweisen der Clickfunktion
btn_berechne = Button(mainform, text="Magie", command=btn_berechne_click)
btn_berechne.pack()

mainform.mainloop()