import random
#fonction qui affiche les règle du jeu
def afficher_regles():
    print("Bienvenue dans le jeu du Juste Prix !")
    print("Le but du jeu est de deviner le prix d'un produit.")
    print("Vous devrez proposer un prix et le programme vous dira si vous êtes trop haut ou trop bas.")
    print("Essayez de trouver le juste prix en utilisant le moins de tentatives possible.")
    print("Bonne chance !")
    print()
    print("Voici comment le jeu fonctionne :")
    print("1. Le programme génère un prix aléatoire entre une plage donnée.")
    print("2. Vous saisissez votre estimation de prix.")
    print("3. Le programme vous indique si votre estimation est trop haute, trop basse ou correcte.")
    print("4. Vous continuez à proposer des estimations jusqu'à trouver le juste prix.")
    print("5. Le programme vous indique le nombre total de tentatives utilisées.")

# fonction qui genère un prix aléatoire
def partie():
 price_mini = 1
 price_max = 100
 price_random = random.randint(price_mini, price_max)
 print(price_random)
 found = False # variable permet d'indiquer si la réponse a été trouvée.

#boucle while qui permet a l'utilisateur de taper le prix qu'il souhaite jusqu'a ce qu'il trouve la bonne réponse.
 while not found:
  number = input("Veuillez entrer un nombre compris entre 1 et 100: ")
  number = int(number)

  if number > price_random:
   print("Le nombre est plus élevé que celui qui a été choisi")
  elif number < price_random:
   print("le nombre est inferieur a celui qui a été choisi")
  else:
   print("Félicitation, tu as trouvé le bon nombre")
   found = True # je remet la variable sur true des que l'utilisateur a trouvé la bonne réponse.

#boucle while pour proposer au joueurs de rejouer si il le souhaite et permet aussi de lancer une partie car les fonctions afficher_regle et partie sont appeller dedans.
continue_game = True
afficher_regles()
while continue_game:
  partie()
  choice = input("voulez vous rejouer une partie ? oui/non :")
  if choice.lower() != "oui":
     continue_game = False
print("Merci d'avoir joué !")

