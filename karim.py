import random

print("Trouver Le prix de l'objet X")
cible = random.randint(1, 10)
#print(f"cible={cible}")

for i in range(5):
 # Récupération de la proposition du joueur
 essai = int(input("votre proposition entre 1 et 10"))

 if essai < 1 or essai > 10:
     print("erreur il faut saisir une valeur entre 1 et 10")
     exit()
 if cible == essai:
     print("bravo")
     break
 elif cible < essai:
     print("trop élevé")
 else :
    print("trop peu")

print("Fin de jeu")
