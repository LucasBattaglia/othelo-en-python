import tkinter as tk
import threading as th
import sqlite3 as sql
from string import *
import random as ran
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fenetre = tk.Tk()

######################################
### connection a la base de donnee ###
######################################

conn = sql.connect('base-de-donnee.db')
cur = conn.cursor()

###############################
###  creation des variable  ###
###############################

largeur_fenetre, hauteur_fenetre = fenetre.winfo_width(), fenetre.winfo_screenheight()
print(largeur_fenetre, hauteur_fenetre)

id = tk.StringVar()
id.set('3')
v = tk.StringVar()
v.set("blue")
v1 = tk.StringVar()
v1.set('')
adresseblanc = tk.StringVar()
adresseblanc.set('')
adressenoir = tk.StringVar()
adressenoir.set('')
v2 = tk.StringVar()
v2.set('')
Vnomblanc = tk.StringVar()
Vnomblanc.set('')
Vnomnoir = tk.StringVar()
Vnomnoir.set('')
MDPnomblanc = tk.StringVar()
MDPnomblanc.set('')
MDPnomnoir = tk.StringVar()
MDPnomnoir.set('')
aff = tk.StringVar()
aff.set('No')
enre = tk.StringVar()
enre.set('No')
code = tk.StringVar()
code.set('')
mdpval = tk.StringVar()
mdpval.set('')
FOND = v.get()
espacement = 0.4
hauteur = 2
largeur = 5
barre_info = tk.Canvas(fenetre, bg="wheat", highlightthickness=0, height=largeur_fenetre, width=150)



###############################
### definition des fonction ###
###############################


def mail(id, nom, adresse, code):
    # on rentre les renseignements pris sur le site du fournisseur
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    # on rentre les informations sur notre adresse e-mail
    email_address = 'developement.python@gmail.com'
    email_password = 'Python123456789'

    # on rentre les informations sur le destinataire
    email_receiver = adresse

    # on crée un e-mail
    message = MIMEMultipart("alternative")
    # on ajoute un sujet
    message["Subject"] = "Validation de votre adresse mail - Othello"
    # un émetteur
    message["From"] = email_address
    # un destinataire
    message["To"] = email_receiver

    # on crée un texte et sa version HTML
    texte = """Bonjour {0}{1}

              Bienvenue sur notre messagerie.
              
              Merci de bien vouloir valider votre adresse mail en allant sur le menu Profil, puis le sous menu verifier un code
              Votre code de verification: {2}
              
              Merci et bonne continuation !

              Notre contact : developement.python@gmail.com
              
              ##########################################
              ### NE PAS REPONDRE - MAIL AUTOMATIQUE ###
              ##########################################
              """.format(nom, id, code)

    html = '''
      <html>
      <body>
      <h1>Bonjour {0}</h1><h4>{1}</h4>
      <pre>
      <h3>Bienvenue sur notre messagerie.</h3>

      Merci de bien vouloir valider votre adresse mail en allant sur le menu Profil, puis le sous menu verifier un code
      Votre code de verification: {2}
              
     Merci et bonne continuation

      Notre contact : developement.python@gmail.com
      </pre>
      </body>
      </html>
      '''.format(nom, id, code)

    # on crée deux éléments MIMEText
    texte_mime = MIMEText(texte, 'plain')
    html_mime = MIMEText(html, 'html')

    # on attache ces deux éléments
    message.attach(texte_mime)
    message.attach(html_mime)

    # on crée la connexion
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # connexion au compte
        server.login(email_address, email_password)
        # envoi du mail
        server.sendmail(email_address, email_receiver, message.as_string())


def valid(Mafenetre):
    cur.execute("SELECT * FROM Joueur WHERE CodeVerification=? AND MDP=?", (code.get(), mdpval.get()))
    profile = cur.fetchall()
    if profile == []:
        print("erreur de code ou de mots de passe")
    else:
        print(profile)
        id=profile[0][0]
        print(id)
        cur.execute("UPDATE Joueur SET AdresseVerifier = 'V' WHERE Id = ?", [id])
        print("Table UPDATE successfully")
        conn.commit()
        Mafenetre.destroy()


def valid_code():
    Mafenetrec = tk.Toplevel()
    codetexte = tk.Label(Mafenetrec, text="Votre code", bg=None)
    codesaisie = tk.Entry(Mafenetrec, textvariable=code, bg='bisque', fg='maroon')
    mdptexte = tk.Label(Mafenetrec, text="Votre mots de passe", bg=None)
    mdpsaisie = tk.Entry(Mafenetrec, textvariable=mdpval, bg='bisque', fg='maroon')
    boutonval = tk.Button(Mafenetrec, text="Valider", command=lambda:valid(Mafenetrec))
    codetexte.grid(row=0, column=0, padx=5, pady=5)
    codesaisie.grid(row=0, column=1, padx=5, pady=5)
    mdptexte.grid(row=1, column=0, padx=5, pady=5)
    mdpsaisie.grid(row=1, column=1, padx=5, pady=5)
    boutonval.grid(row=2, column=1, padx=5, pady=5)


def generateur_dmdp():
    smdp = ascii_letters + digits
    nmpd = ''.join(ran.choice(smdp) for i in range(ran.randint(6, 9)))
    print(nmpd)
    return nmpd


def affichage_table():
    if aff.get() == "Yes":
        barre_info.grid(row=0, column=0, padx=5, pady=5, rowspan=5)

        InfoBlanc = tk.Label(barre_info, text="Joueur Blanc", font=("Ink Free", 20), bg='wheat', fg="black")
        info_nom_B = tk.Label(barre_info, text="Nom : ", font=("Ink Free", 20), bg='wheat', fg="black")
        info_nom_Blanc = tk.Label(barre_info, textvariable=Vnomblanc.get(), font=("Ink Free", 20), bg='wheat', fg="black")
        InfoNoir = tk.Label(barre_info, text="Joueur Noir", font=("Ink Free", 20), bg='wheat', fg="black")
        info_nom_N = tk.Label(barre_info, text="Nom : ", font=("Ink Free", 20), bg='wheat', fg="black")
        info_nom_Noir = tk.Label(barre_info, textvariable=Vnomnoir.get(), font=("Ink Free", 20), bg='wheat', fg="black")
        InfoBlanc.grid(row=0, column=0, padx=5, pady=5)
        info_nom_B.grid(row=1, column=0, padx=5, pady=5)
        info_nom_Blanc.grid(row=1, column=1, padx=5, pady=5)
        InfoNoir.grid(row=2, column=0, padx=5, pady=5)
        info_nom_N.grid(row=3, column=0, padx=5, pady=5)
        info_nom_Noir.grid(row=3, column=1, padx=5, pady=5)
    elif aff.get() == "No":
        barre_info.grid_forget()
        print("cachage")


def Conf_joueur():
    def colorinterface():
        while True:
            Mafenetrej.configure(background=v.get())
            for c in Mafenetrej.winfo_children():
                if type(c) is not tk.Canvas:
                    c['bg'] = v.get()
                if type(c) is tk.Label or type(c) is tk.Radiobutton or type(c) is tk.Button:
                    if v.get() == "white":
                        c['fg'] = "black"
                    elif v.get() == "blue":
                        c['fg'] = 'Yellow'
                    elif v.get() == "black":
                        c['fg'] = 'white'
                    if type(c) is tk.Radiobutton:
                        c['selectcolor'] = v.get()

    def text():
        print("v1=", v1.get(), "v2=", v2.get())
        if v1.get() == "Inscription" or v2.get() == "Inscription":
            print("v1 inscription")
            id.grid(row=1, column=0, padx=5, pady=5)
            Motsdepasse.grid(row=2, column=0, padx=5, pady=5)
            Adresse.grid(row=3, column=0, padx=5, pady=5)
        elif v1.get() == "Oui" or v2.get() == "Oui":
            print("v1 Oui")
            id.grid(row=1, column=0, padx=5, pady=5)
            Motsdepasse.grid(row=2, column=0, padx=5, pady=5)
            Adresse.grid_forget()
        else:
            print("sinon")
            id.grid_forget()
            Motsdepasse.grid_forget()
            Adresse.grid_forget()

    def database(nom,mdp,adresse,code):
        try:
            cur.execute("SELECT MAX(Id) FROM Joueur;")
            id = cur.fetchall()[0][0] + 1
        except:
            id = 000
        cur.execute("INSERT INTO Joueur VALUES (?, ?, ?, ?, 'X', ? )", [id, nom, mdp, adresse, code])
        print("Table created successfully")
        conn.commit()

    def enregistrementb():
        nom = '{}'.format(Vnomblanc.get())
        mdp = '{}'.format(MDPnomblanc.get())
        adresse = '{}'.format(adresseblanc.get())
        code = '{}'.format(generateur_dmdp()[0:6])
        mail(id, nom, adresse, code)
        print("id:{}\nnom:{}\nmots de passe:{}\nadresse:{}\ncode:{}".format(id, nom, mdp, adresse, code))
        database(nom,mdp,adresse,code)
        idblanc.grid(row=1, column=1, padx=5, pady=5)
        Motsdepasseb.grid(row=2, column=1, padx=5, pady=5)
        Adresse.grid_forget()
        Adresseb.grid_forget()
        enregistrementblanc.grid_forget()
        v1.set('Oui')



    def connectonblanc():
        if v1.get() == "Oui":
            idblanc.grid(row=1, column=1, padx=5, pady=5)
            Motsdepasseb.grid(row=2, column=1, padx=5, pady=5)
            Adresseb.grid_forget()
        elif v1.get() == "Inscription":
            Vnomblanc.set('')
            MDPnomblanc.set('')
            adresseblanc.set('')
            idblanc.grid(row=1, column=1, padx=5, pady=5)
            Motsdepasseb.grid(row=2, column=1, padx=5, pady=5)
            Adresseb.grid(row=3, column=1, padx=5, pady=5)
            enregistrementblanc.grid(row=8, column=1, padx=5, pady=5)
        else:
            idblanc.grid_forget()
            Motsdepasseb.grid_forget()
            Adresseb.grid_forget()
        text()

    def enregistrementn():
        nom = '{}'.format(Vnomnoir.get())
        mdp = '{}'.format(MDPnomnoir.get())
        adresse = '{}'.format(adressenoir.get())
        code = '{}'.format(generateur_dmdp()[0:6])
        mail(id, nom, adresse, code)
        print("id:{}\nnom:{}\nmots de passe:{}\nadresse:{}\ncode:{}".format(id, nom, mdp, adresse, code))
        database(nom,mdp,adresse,code)
        idnoir.grid(row=1, column=2, padx=5, pady=5)
        Motsdepassen.grid(row=2, column=2, padx=5, pady=5)
        Adresse.grid_forget()
        Adressen.grid_forget()
        enregistrementnoir.grid_forget()
        v2.set('Oui')

    def connectonnoir():
        if v2.get() == "Oui":
            idnoir.grid(row=1, column=2, padx=5, pady=5)
            Motsdepassen.grid(row=2, column=2, padx=5, pady=5)
            Adressen.grid_forget()
        elif v2.get() == "Inscription":
            Vnomnoir.set('')
            MDPnomnoir.set('')
            adressenoir.set('')
            idnoir.grid(row=1, column=2, padx=5, pady=5)
            Motsdepassen.grid(row=2, column=2, padx=5, pady=5)
            Adressen.grid(row=3, column=2, padx=5, pady=5)
            enregistrementnoir.grid(row=8, column=2, padx=5, pady=5)
        else:
            idnoir.grid_forget()
            Motsdepassen.grid_forget()
            Adressen.grid_forget()
        text()


    # Création de la fenêtre principale (main window)
    Mafenetrej = tk.Toplevel()
    Mafenetrej.title("Configuration des joueur")

    # creation de thread pour le changement de couleur
    th1 = th.Thread(target=colorinterface)
    th1.start()

    Blanc = tk.Label(Mafenetrej, text='Joueur BLANC ')
    Blanc.grid(row=0, column=1, padx=5, pady=5)

    Noir = tk.Label(Mafenetrej, text='Joueur NOIR ')
    Noir.grid(row=0, column=2, padx=5, pady=5)

    id = tk.Label(Mafenetrej, text='Identifiant')

    idblanc = tk.Entry(Mafenetrej, textvariable=Vnomblanc, bg='bisque', fg='maroon')

    idnoir = tk.Entry(Mafenetrej, textvariable=Vnomnoir, bg='bisque', fg='maroon')

    Motsdepasse = tk.Label(Mafenetrej, text='Mots de passe')

    Motsdepasseb = tk.Entry(Mafenetrej, textvariable=MDPnomblanc, bg='bisque', fg='maroon')

    Motsdepassen = tk.Entry(Mafenetrej, textvariable=MDPnomnoir, bg='bisque', fg='maroon')

    Adresse = tk.Label(Mafenetrej, text='Adresse mail')

    Adresseb = tk.Entry(Mafenetrej, textvariable=adresseblanc, bg='bisque', fg='maroon')

    Adressen = tk.Entry(Mafenetrej, textvariable=adressenoir, bg='bisque', fg='maroon')

    j1 = tk.Radiobutton(Mafenetrej, text="jouer contre l'ordinateur", variable=v1, value="IA", command=connectonblanc,
                        bg=None)
    j1.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
    j1.deselect()
    j2 = tk.Radiobutton(Mafenetrej, text="ne pas connecter ce joueur", variable=v1, value='Non', command=connectonblanc,
                        bg=None)
    j2.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
    j3 = tk.Radiobutton(Mafenetrej, text="connecter ce joueur", variable=v1, value='Oui', command=connectonblanc,
                        bg=None)
    j3.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
    j4 = tk.Radiobutton(Mafenetrej, text="inscrire ce joueur", variable=v1, value="Inscription", command=connectonblanc,
                        bg=None)
    j4.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)
    enregistrementblanc = tk.Button(Mafenetrej, text="enregisrer", command=enregistrementb)

    j5 = tk.Radiobutton(Mafenetrej, text="jouer contre l'ordinateur", variable=v2, value="IA", command=connectonnoir,
                        bg=None)
    j5.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
    j5.deselect()
    j6 = tk.Radiobutton(Mafenetrej, text="ne pas connecter ce joueur", variable=v2, value="Non", command=connectonnoir,
                        bg=None)
    j6.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W)
    j7 = tk.Radiobutton(Mafenetrej, text="connecter ce joueur", variable=v2, value="Oui", command=connectonnoir,
                        bg=None)
    j7.grid(row=6, column=2, padx=5, pady=5, sticky=tk.W)
    j8 = tk.Radiobutton(Mafenetrej, text="inscrire ce joueur", variable=v2, value="Inscription", command=connectonnoir,
                        bg=None)
    j8.grid(row=7, column=2, padx=5, pady=5, sticky=tk.W)
    enregistrementnoir = tk.Button(Mafenetrej, text="enregisrer", command=enregistrementn)




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
        Mafenetrei.configure(background=v.get())
        for c in Mafenetrei.winfo_children():
            if type(c) is not tk.Canvas:
                c['bg'] = v.get()
                if type(c) is tk.Radiobutton:
                    c['selectcolor'] = v.get()
                if v.get() == "white":
                    c['fg'] = "black"
                elif v.get() == "blue":
                    c['fg'] = 'Yellow'
                elif v.get() == "black":
                    c['fg'] = 'white'

    # Création de la fenêtre principale (main window)
    Mafenetrei = tk.Toplevel()
    Mafenetrei.title("Configuration de l'interface")
    Mafenetrei.configure(bg=None)

    Label1 = tk.Label(Mafenetrei, text="Theme de Fond", bg=None)
    Label1.grid(row=0, column=0, padx=5, pady=5)

    r1 = tk.Radiobutton(Mafenetrei, text="Par défaut", variable=v, value="blue", command=sel, bg=None)
    r1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    r2 = tk.Radiobutton(Mafenetrei, text="Clair", variable=v, value="white", command=sel, bg=None)
    r2.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    r3 = tk.Radiobutton(Mafenetrei, text="Sombre", variable=v, value="black", command=sel, bg=None)
    r3.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    Label2 = tk.Label(Mafenetrei, text="Barre d'information", bg=None)
    Label2.grid(row=0, column=1, padx=5, pady=5)

    b1 = tk.Radiobutton(Mafenetrei, text="Oui", variable=aff, value='Yes', indicatoron=0, command=affichage_table,
                        bg=None)
    b1.grid(row=1, column=1, padx=5, pady=5)
    b2 = tk.Radiobutton(Mafenetrei, text="Non", variable=aff, value='No', indicatoron=0, command=affichage_table,
                        bg=None)
    b2.grid(row=2, column=1, padx=5, pady=5)

    Label3 = tk.Label(Mafenetrei, text="Enregistrer la configuration\npour la prochaine fois", bg=None)
    Label3.grid(row=0, column=2, padx=5, pady=5)

    b3 = tk.Radiobutton(Mafenetrei, text="Oui", variable=enre, value='V', indicatoron=0, command=enre.get,
                        bg=None)
    b3.grid(row=1, column=2, padx=5, pady=5)
    b4 = tk.Radiobutton(Mafenetrei, text="Non", variable=enre, value='X', indicatoron=0, command=enre.get,
                        bg=None)
    b4.grid(row=2, column=2, padx=5, pady=5)

def quitter():
    conn.close()
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

profil_menu = tk.Menu(menu_bar, tearoff=0)
profil_menu.add_command(label="valider un code", command=valid_code)

quit_menu = tk.Menu(menu_bar, tearoff=0)
quit_menu.add_command(label="Quitter", command=quitter)

menu_bar.add_cascade(label="Configuration", menu=Conf_menu)
menu_bar.add_cascade(label="Profil", menu=profil_menu)
menu_bar.add_cascade(label="Deconnection", menu=quit_menu)

fenetre.config(menu=menu_bar)

fenetre.mainloop()
