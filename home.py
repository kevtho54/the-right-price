import random
from tkinter import Tk, Canvas, Button, Listbox, Scrollbar, END, Entry, Label, Frame

event_listbox = None  # Variable globale pour la liste d'événements
entry_guess = None
tentative_label = None
tentative = 10

# Fonction qui affiche les règles du jeu
def afficher_regles(canvas):
    # Code pour afficher les règles
   canvas.create_text(300,80,text="Bienvenue dans le jeu du Juste Prix !")
   canvas.create_text(300,100,text="Le but du jeu est de deviner le prix que l'ordinateur a choisi.")
   canvas.create_text(300,120,text="Tu devras proposer un prix et le programme te diras si tu es trop haut ou trop bas.")
   canvas.create_text(300,140,text="Essaye de trouver le juste prix en utilisant le moins de tentatives possible.")
   canvas.create_text(300,160,text="Bonne chance !")
   canvas.create_text(300,180,text="Voici comment le jeu fonctionne :")
   canvas.create_text(300,200,text="1. Le programme génère un prix aléatoire entre 1 et 100.")
   canvas.create_text(300,220,text="2. Tu saisi une estimation de prix.")
   canvas.create_text(300,240,text="3. Le programme t'indique si ton estimation est trop haute, trop basse ou correcte.")
   canvas.create_text(300,260,text="4. Tu continues à proposer des estimations jusqu'à trouver le juste prix.")
   canvas.create_text(300,280,text="Tu as un total de 6 tentatives.")
   canvas.create_text(300,300,text="5. Le programme t'indique le nombre de tentatives restante.")
   canvas.create_text(300,320,text="Bon jeu")


#La fonction est appeler quand l'utilisateur clique sur le bouton demarrer le jeu
def start_game():
    # Supprime le contenu du canvas
    canvas.pack_forget()
    start_button.pack_forget()
    # Affiche les éléments nécessaires pour le jeu : entry_guess, validate_button
    entry_guess.pack(pady=10)
    validate_button.pack()
    tentative_label.pack(pady=10)
    frame_evenements.pack(side="top", fill="both", expand=True, padx=10, pady=10)
    event_listbox.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
   

    # Appelle la fonction new_game
    new_game()

# Fonction qui gère le déroulement du jeu
def partie():
    global tentative
    # Définit number en récupérant la valeur de entry_guess et en la convertissant en entier
    number = int(entry_guess.get())
    add_event(number)

    # Vérifie si number est un nombre valide (entier)
    # Si ce n'est pas le cas, affiche un message d'erreur dans event_listbox
    if not str(number).isdigit():
        add_event("Erreur : Veuillez entrer un nombre valide.")
        return
    # Vérifie si number est compris entre 1 et 100
    if number < 1 or number > 100:
        add_event("Erreur ! Le nombre que tu as choisi ne figure pas entre 1 et 100")
        return
    #Compare number avec price_random pour déterminer si c'est trop haut, trop bas ou correct
    if number > price_random:
        add_event("C'est moins !!")
    elif number < price_random:
        add_event("C'est plus !!")
    else:
        add_event("C'est gagné ! Félicitation !")
        validate_button.pack_forget()
        
        return
    #Décrémente le compteur a chaque fois qu'une réponse est mauvaise
    tentative -= 1
    tentative_label.config(text="Nombre de tentatives restantes : " + str(tentative))
    #Vérifie si le compteur est a 0, une fois a 0 le jeu est perdu
    if tentative == 0:
        add_event("Mince, tu as perdu !! Le chiffre était : " +  str(price_random))
        start_button.pack(pady= 10)
        return
    #Efface le contenu de entry_guess et met le focus sur l'entrée
    entry_guess.delete(0, END)
    # Cela permet à l'utilisateur de saisir une nouvelle estimation
    entry_guess.focus()

# Fonction qui valide la proposition de l'utilisateur
def validate_guess(event=None):
    # Appelle la fonction partie pour gérer la proposition de l'utilisateur
    partie()

# Fonction qui ajoute un événement à la liste
def add_event(event):
     # Utilise la méthode insert de event_listbox pour ajouter un événement à la fin de la liste
    event_listbox.insert(END, event)

# Fonction pour commencer une nouvelle partie
def new_game():
    global price_random, tentative
    #genere un nouveau prix aléatoire entre 1 et 100
    price_random = random.randint(1, 100)
    #Initialise le nombre de tentative a 10
    tentative = 6
    #Met à jour le texte de tentative_label pour afficher le nombre de tentatives restantes
    tentative_label.config(text="Nombre de tentatives restantes : " + str(tentative))
    # Efface le contenu de event_listbox
    event_listbox.delete(0, END)


#Crée une fenêtre tkinter


fenetre = Tk()
fenetre.geometry("800x600")
fenetre.title("Le juste prix")

canvas = Canvas(fenetre, width=600, height=400)
canvas.pack()

frame_evenements = Frame(fenetre)
frame_evenements.pack(side="top", fill="both", expand=True, padx=10, pady=10)
frame_evenements.pack_forget()

event_listbox = Listbox(frame_evenements)
event_listbox.pack(side="top", fill="both", expand=True)
#event_listbox.config(width=100, height=100)
event_listbox.pack_forget()

scrollbar = Scrollbar(frame_evenements)
scrollbar.pack(side="right", fill="y")
event_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=event_listbox.yview)
scrollbar.pack_forget()

entry_guess = Entry(fenetre, width=40)
entry_guess.pack(pady=10)
entry_guess.pack_forget()

validate_button = Button(fenetre, text="Valider", command=validate_guess)
validate_button.pack(pady=10)
validate_button.pack_forget()

tentative = 10  # Exemple de valeur pour la variable tentative
tentative_label = Label(fenetre, text="Nombre de tentatives restantes : " + str(tentative))
tentative_label.pack(pady=30)
tentative_label.pack_forget()

afficher_regles(canvas)

start_button = Button(fenetre, text="Démarrer le jeu", command=start_game)
start_button.pack()

entry_guess.bind("<Return>", validate_guess)

fenetre.mainloop()