import random
#fonction qui affiche les règle du jeu
def afficher_regles():
    print("Bienvenue dans le jeu du Juste Prix !")
    print("Le but du jeu est de deviner le prix que l'ordinateur a choisi.")
    print("Vous devrez proposer un prix et le programme vous dira si vous êtes trop haut ou trop bas.")
    print("Essayez de trouver le juste prix en utilisant le moins de tentatives possible.")
    print("Bonne chance !")
    print("Voici comment le jeu fonctionne :")
    print("1. Le programme génère un prix aléatoire entre 1 et 100.")
    print("2. Vous saisissez votre estimation de prix.")
    print("3. Le programme vous indique si votre estimation est trop haute, trop basse ou correcte.")
    print("4. Vous continuez à proposer des estimations jusqu'à trouver le juste prix.")
    print("5. Le programme vous indique le nombre de tentatives restante.")
    print( "Bon jeu!")

# fonction qui genère un prix aléatoire
def partie():
 price_mini = 1
 price_max = 100
 price_random = random.randint(price_mini, price_max)
 print(price_random)
 tentative = 10
 print("Tu as un total de 10 tentatives, bonne chance !")
 found = False # variable permet d'indiquer si la réponse a été trouvée.

#boucle while qui permet a l'utilisateur de taper le prix qu'il souhaite jusqu'a ce qu'il trouve la bonne réponse.
 while not found:
  number = input("Veuillez entrer un nombre compris entre 1 et 100: ")
  #condition qui permet d'afficher une erreur si la touche entrée par l'utilisateur n'est pas un chiffre.
  if not number.isdigit():
    print("Erreur : Veuillez entrer un nombre valide.")
    continue

  number = int(number)

  if number < price_mini or number > price_max:
   print("Erreur ! Le nombre que tu as choisi ne figure pas entre 1 et 100")
   continue

 
  if number > price_random:
   tentative -= 1
   print("c'est moins !!")
   print ("Nombre de tentative restante: ", tentative)
   

  elif number < price_random:
   tentative -= 1
   print("c'est plus !!")
   print ("Nombre de tentative restante: ", tentative)
   
  else:
   print("c'est gagné ! Félicitation !")
   found = True # je remet la variable sur true des que l'utilisateur a trouvé la bonne réponse.


  if tentative == 0:
   break
  
 if not found:
  print("Mince, tu as perdu !!")
  



#boucle while pour proposer au joueurs de rejouer si il le souhaite et permet aussi de lancer une partie car les fonctions afficher_regle et partie sont appeller dedans.
continue_game = True
afficher_regles()
while continue_game:
  partie()
  choice = input("veux-tu rejouer une partie ? oui/non :")
  if choice.lower() != "oui":
     continue_game = False
print("Merci d'avoir joué !")

