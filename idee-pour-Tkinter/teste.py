from tkinter import*
fen = Tk()
fen.title('OTHELLO')
fen.configure(background = "black")

def mouseClic(event):
    print("mouseClic")
    # A la création de la grille de jeu on affiche sur le canvas 8x8 carrés.
    # Dans chaque carré on dessine un cercle figurant le pion; ce cercle est
    # de la même couleur que le fond, ce qui le rend invisible. Pour afficher
    # un pion, il suffit de modifier sa couleur.
    y = 1
    for lg in range(1, 9):
        x = 1
        for cl in range(1, 9):
            can.create_rectangle(x, y, x + 59, y + 59)
            x += 60
        y += 60


def passe():
    print("passe")

def nouveauJeu():
    print("nouveauJeu")
    # A la création de la grille de jeu on affiche sur le canvas 8x8 carrés.
    # Dans chaque carré on dessine un cercle figurant le pion; ce cercle est
    # de la même couleur que le fond, ce qui le rend invisible. Pour afficher
    # un pion, il suffit de modifier sa couleur.
    y = 1
    for lg in range(1, 9):
        x = 1
        for cl in range(1, 9):
            can.create_rectangle(x, y, x + 59, y + 59)
            x += 60
        y += 60


def handicap():
    print("handicap")

def aide():
    print("aide")

fr1 =Frame(fen,bd =2, relief=SOLID, bg = "black")
b1 = Button(fr1,text="Nouvelle partie",font="Arial 12",width =15,
                    command = nouveauJeu)
b1.pack(side = LEFT, padx =10, pady = 5)
b2 = Button(fr1,text="Handicap",font="Arial 12",width =15,
                    command = handicap)
b2.pack(side = LEFT, padx =10, pady = 5)
b3 = Button(fr1,text="Aide",font="Arial 12",width =15, command = aide)
b3.pack(side = LEFT, padx =10, pady = 5)
fr1.pack()

can = Canvas(fen, bg="#009000", width=476, height=476, bd=2, relief=SOLID)
can.bind("<Button-1>", mouseClic)
can.pack(padx=5, pady=5)

fr2 =Frame(fen,bd =2, relief=SOLID, bg = "black")
mess = Label(fr2, width=40, bg = "white", font="Arial 12")
mess.pack(side=LEFT, padx=5, pady=5)
bp = Button(fr2,text="Passe",font="Arial 12",width =11,
                   command = passe)
bp.pack(side=RIGHT,padx=5,pady=5)
fr2.pack()

fr3 =Frame(fen,bd =2, relief=SOLID, bg = "black")
nbb = Label(fr3, text="Blancs : 2", width = 16, bg = "white", font="Arial 12")
nbb.pack(side=LEFT, padx=6, pady=5)
nbn = Label(fr3, text="Noirs : 2", width = 16, bg = "white",font="Arial 12")
nbn .pack(side=LEFT, padx=6, pady=5)
nbr = Label(fr3, text="Reste : 60", width = 17, bg = "white",font="Arial 12")
nbr.pack(side=LEFT, padx=6, pady=5)
fr3.pack()

fen.mainloop()