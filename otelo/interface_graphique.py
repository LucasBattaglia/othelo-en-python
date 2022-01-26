import tkinter as tk
import time as t

fenetre = tk.Tk()

###############################
###  creation des variable  ###
###############################

largeur_fenetre, hauteur_fenetre = fenetre.winfo_width(), fenetre.winfo_screenheight()
print(largeur_fenetre, hauteur_fenetre)

v = tk.StringVar()
v.set("blue")
v1 = tk.StringVar()
v1.set("")
v2 = tk.StringVar()
v2.set("")
Vnomblanc = tk.StringVar()
Vnomblanc.set("")
Vnomnoir = tk.StringVar()
Vnomnoir.set("")
MDPnomblanc = tk.StringVar()
MDPnomblanc.set("")
MDPnomnoir = tk.StringVar()
MDPnomnoir.set("")
aff = tk.StringVar()
aff.set("No")
FOND = v.get()
espacement = 0.4
hauteur = 2
largeur = 5
barre_info = tk.Canvas(fenetre, bg="light yellow", highlightthickness=0, height=largeur_fenetre, width=150)


###############################
### definition des fonction ###
###############################

def affichage_table():
    if aff.get() == "Yes":
        barre_info.grid(row=0, column=0, padx=5, pady=5, rowspan=5)
        print("affichage")
    elif aff.get() == "No":
        barre_info.grid_forget()
        print("cachage")


def Conf_joueur():
    # Création de la fenêtre principale (main window)
    Mafenetre = tk.Toplevel()
    Mafenetre.title("Configuration des joueur")

    Blanc = tk.Label(Mafenetre, text='Joueur BLANC ')
    Blanc.grid(row=0, column=1, padx=5, pady=5)

    Noir = tk.Label(Mafenetre, text='Joueur NOIR ')
    Noir.grid(row=0, column=2, padx=5, pady=5)

    id = tk.Label(Mafenetre, text='Identifiant')
    id.grid(row=1, column=0, padx=5, pady=5)

    idblanc = tk.Entry(Mafenetre, textvariable=Vnomblanc, bg='bisque', fg='maroon')
    idblanc.grid(row=1, column= 1, padx=5, pady=5)

    idnoir = tk.Entry(Mafenetre, textvariable=Vnomnoir, bg='bisque', fg='maroon')
    idnoir.grid(row=1, column=2, padx=5, pady=5)

    Motsdepasse = tk.Label(Mafenetre, text='Mots de passe')
    Motsdepasse.grid(row=2, column=0, padx=5, pady=5)

    Motsdepasseb = tk.Entry(Mafenetre, textvariable=MDPnomblanc, bg='bisque', fg='maroon')
    Motsdepasseb.grid(row=2, column=1, padx=5, pady=5)

    Motsdepassen = tk.Entry(Mafenetre, textvariable=MDPnomnoir, bg='bisque', fg='maroon')
    Motsdepassen.grid(row=2, column=2, padx=5, pady=5)

    j1 = tk.Radiobutton(Mafenetre, text="jouer contre l'ordinateur", variable=v1, value="IA", command=v1.get, bg=None)
    j1.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
    j2 = tk.Radiobutton(Mafenetre, text="ne pas connecter ce joueur", variable=v1, value="Non", command=v1.get, bg=None)
    j2.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
    j3 = tk.Radiobutton(Mafenetre, text="connecter ce joueur", variable=v1, value="Oui", command=v1.get, bg=None)
    j3.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

    j4 = tk.Radiobutton(Mafenetre, text="jouer contre l'ordinateur", variable=v2, value="IA", command=v2.get, bg=None)
    j4.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)
    j5 = tk.Radiobutton(Mafenetre, text="ne pas connecter ce joueur", variable=v2, value="Non", command=v2.get, bg=None)
    j5.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
    j6 = tk.Radiobutton(Mafenetre, text="connecter ce joueur", variable=v2, value="Oui", command=v1.get, bg=None)
    j6.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W)


def Conf_interface():
    def sel():
        fenetre.configure(background=v.get())
        for c in fenetre.winfo_children():
            if type(c) is not tk.Canvas:
                c['bg'] = v.get()
                if type(c) is tk.Label:
                    if v.get() == "white":
                        c['fg'] = "black"
                    elif v.get() == "blue":
                        c['fg'] = 'Yellow'
                    elif v.get() == "black":
                        c['fg'] = 'white'
        Mafenetre.configure(background=v.get())
        for c in Mafenetre.winfo_children():
            if type(c) is not tk.Canvas:
                c['bg'] = v.get()
                if type(c) is tk.Radiobutton:
                    print(c['selectcolor'])
                    c['selectcolor'] = v.get()
                if v.get() == "white":
                    c['fg'] = "black"
                elif v.get() == "blue":
                    c['fg'] = 'Yellow'
                elif v.get() == "black":
                    c['fg'] = 'white'

    # Création de la fenêtre principale (main window)
    Mafenetre = tk.Toplevel()
    Mafenetre.title("Configuration de l'interface")
    Mafenetre.configure(bg=None)

    Label1 = tk.Label(Mafenetre, text="Theme de Fond", bg=None)
    Label1.grid(row=0, column=0, padx=5, pady=5)

    r1 = tk.Radiobutton(Mafenetre, text="Par défaut", variable=v, value="blue", command=sel, bg=None)
    r1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    r2 = tk.Radiobutton(Mafenetre, text="Clair", variable=v, value="white", command=sel, bg=None)
    r2.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    r3 = tk.Radiobutton(Mafenetre, text="Sombre", variable=v, value="black", command=sel, bg=None)
    r3.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    Label1 = tk.Label(Mafenetre, text="Barre d'information", bg=None)
    Label1.grid(row=0, column=1, padx=5, pady=5)

    b1 = tk.Radiobutton(Mafenetre, text="Oui", variable=aff, value="Yes", indicatoron=0, command=affichage_table,
                        bg=None)
    b1.grid(row=1, column=1, padx=5, pady=5)
    b2 = tk.Radiobutton(Mafenetre, text="Non", variable=aff, value="No", indicatoron=0, command=affichage_table,
                        bg=None)
    b2.grid(row=2, column=1, padx=5, pady=5)


def quitter():
    fenetre.destroy()


###############################
###  Programme  principale  ###
###############################

# creation de la fenetre:
fenetre.configure(background=FOND)
fenetre.title('Othelo')

titre = tk.Label(fenetre, text="Othelo", font=("Ink Free", 20), bg=FOND, fg="Yellow")
titre.grid(row=0, column=1, padx=5, pady=5)

Canevas = tk.Canvas(fenetre, bg="black", highlightthickness=0)
Canevas.grid(row=1, column=1, padx=5, pady=5)

bouton11 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton12 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton13 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton14 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton15 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton16 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton17 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton18 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton11.grid(row=0, column=0, padx=espacement, pady=espacement)
bouton12.grid(row=0, column=1, padx=espacement, pady=espacement)
bouton13.grid(row=0, column=2, padx=espacement, pady=espacement)
bouton14.grid(row=0, column=3, padx=espacement, pady=espacement)
bouton15.grid(row=0, column=4, padx=espacement, pady=espacement)
bouton16.grid(row=0, column=5, padx=espacement, pady=espacement)
bouton17.grid(row=0, column=6, padx=espacement, pady=espacement)
bouton18.grid(row=0, column=7, padx=espacement, pady=espacement)

bouton21 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton22 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton23 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton24 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton25 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton26 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton27 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton28 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton21.grid(row=1, column=0, padx=espacement, pady=espacement)
bouton22.grid(row=1, column=1, padx=espacement, pady=espacement)
bouton23.grid(row=1, column=2, padx=espacement, pady=espacement)
bouton24.grid(row=1, column=3, padx=espacement, pady=espacement)
bouton25.grid(row=1, column=4, padx=espacement, pady=espacement)
bouton26.grid(row=1, column=5, padx=espacement, pady=espacement)
bouton27.grid(row=1, column=6, padx=espacement, pady=espacement)
bouton28.grid(row=1, column=7, padx=espacement, pady=espacement)

bouton31 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton32 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton33 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton34 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton35 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton36 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton37 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton38 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton31.grid(row=2, column=0, padx=espacement, pady=espacement)
bouton32.grid(row=2, column=1, padx=espacement, pady=espacement)
bouton33.grid(row=2, column=2, padx=espacement, pady=espacement)
bouton34.grid(row=2, column=3, padx=espacement, pady=espacement)
bouton35.grid(row=2, column=4, padx=espacement, pady=espacement)
bouton36.grid(row=2, column=5, padx=espacement, pady=espacement)
bouton37.grid(row=2, column=6, padx=espacement, pady=espacement)
bouton38.grid(row=2, column=7, padx=espacement, pady=espacement)

bouton41 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton42 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton43 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton44 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton45 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton46 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton47 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton48 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton41.grid(row=3, column=0, padx=espacement, pady=espacement)
bouton42.grid(row=3, column=1, padx=espacement, pady=espacement)
bouton43.grid(row=3, column=2, padx=espacement, pady=espacement)
bouton44.grid(row=3, column=3, padx=espacement, pady=espacement)
bouton45.grid(row=3, column=4, padx=espacement, pady=espacement)
bouton46.grid(row=3, column=5, padx=espacement, pady=espacement)
bouton47.grid(row=3, column=6, padx=espacement, pady=espacement)
bouton48.grid(row=3, column=7, padx=espacement, pady=espacement)

bouton51 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton52 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton53 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton54 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton55 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton56 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton57 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton58 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton51.grid(row=4, column=0, padx=espacement, pady=espacement)
bouton52.grid(row=4, column=1, padx=espacement, pady=espacement)
bouton53.grid(row=4, column=2, padx=espacement, pady=espacement)
bouton54.grid(row=4, column=3, padx=espacement, pady=espacement)
bouton55.grid(row=4, column=4, padx=espacement, pady=espacement)
bouton56.grid(row=4, column=5, padx=espacement, pady=espacement)
bouton57.grid(row=4, column=6, padx=espacement, pady=espacement)
bouton58.grid(row=4, column=7, padx=espacement, pady=espacement)

bouton61 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton62 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton63 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton64 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton65 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton66 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton67 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton68 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton61.grid(row=5, column=0, padx=espacement, pady=espacement)
bouton62.grid(row=5, column=1, padx=espacement, pady=espacement)
bouton63.grid(row=5, column=2, padx=espacement, pady=espacement)
bouton64.grid(row=5, column=3, padx=espacement, pady=espacement)
bouton65.grid(row=5, column=4, padx=espacement, pady=espacement)
bouton66.grid(row=5, column=5, padx=espacement, pady=espacement)
bouton67.grid(row=5, column=6, padx=espacement, pady=espacement)
bouton68.grid(row=5, column=7, padx=espacement, pady=espacement)

bouton71 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton72 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton73 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton74 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton75 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton76 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton77 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton78 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton71.grid(row=6, column=0, padx=espacement, pady=espacement)
bouton72.grid(row=6, column=1, padx=espacement, pady=espacement)
bouton73.grid(row=6, column=2, padx=espacement, pady=espacement)
bouton74.grid(row=6, column=3, padx=espacement, pady=espacement)
bouton75.grid(row=6, column=4, padx=espacement, pady=espacement)
bouton76.grid(row=6, column=5, padx=espacement, pady=espacement)
bouton77.grid(row=6, column=6, padx=espacement, pady=espacement)
bouton78.grid(row=6, column=7, padx=espacement, pady=espacement)

bouton81 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton82 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton83 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton84 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton85 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton86 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton87 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton88 = tk.Button(Canevas, text="     ", bg="Green", height=hauteur, width=largeur)
bouton81.grid(row=7, column=0, padx=espacement, pady=espacement)
bouton82.grid(row=7, column=1, padx=espacement, pady=espacement)
bouton83.grid(row=7, column=2, padx=espacement, pady=espacement)
bouton84.grid(row=7, column=3, padx=espacement, pady=espacement)
bouton85.grid(row=7, column=4, padx=espacement, pady=espacement)
bouton86.grid(row=7, column=5, padx=espacement, pady=espacement)
bouton87.grid(row=7, column=6, padx=espacement, pady=espacement)
bouton88.grid(row=7, column=7, padx=espacement, pady=espacement)

erreur = tk.StringVar()
erreur.set("")
texterreur = tk.Label(fenetre, textvariable=erreur, font=("Ink Free", 20), bg=FOND, fg="Yellow")
texterreur.grid(row=2, column=1, padx=5, pady=5)

menu_bar = tk.Menu(fenetre)

Conf_menu = tk.Menu(menu_bar, tearoff=0)
Conf_menu.add_command(label="Joueur", command=Conf_joueur)

inter_menu = tk.Menu(menu_bar, tearoff=0)
Conf_menu.add_command(label="Interface", command=Conf_interface)

quit_menu = tk.Menu(menu_bar, tearoff=0)
quit_menu.add_command(label="Quitter", command=quitter)

menu_bar.add_cascade(label="Configuration", menu=Conf_menu)
menu_bar.add_cascade(label="Deconnection", menu=quit_menu)

fenetre.config(menu=menu_bar)

fenetre.mainloop()
