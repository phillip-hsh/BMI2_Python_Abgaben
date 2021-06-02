from tkinter import *

def btn_einloggen_click():
    benutzer = str(txt_benutzer.get())
    passwort = str(txt_passwort.get())

    newWindow = Toplevel(login)
    newWindow.title("Antwort")
    label_user = Label(newWindow, text = benutzer)
    label_user.pack()

    label_passwd = Label(newWindow, text = passwort)
    label_passwd.pack()

    label_result = Label(newWindow)
    label_result.pack()


    if benutzer == 'ma' and passwort == '123':
        label_result["text"] = 'LOGIN geglückt'
    
    else:
        label_result["text"] = 'LOGIN Fehlgeschlagen'

     # Modales Verhalten erzeugen
    newWindow.grab_set()

    # ## Testkommentar
    
login = Tk()
login.title("Login")
login.geometry("250x140")

txt_benutzer = Entry(login)
txt_benutzer.pack()

txt_passwort = Entry(login, show="*")
txt_passwort.pack()

btn_einloggen = Button(login, text="Magie", command=btn_einloggen_click)
btn_einloggen.pack()

login.mainloop()