import random

print("Trouver Le prix de l'objet X")
cible = random.randint(1, 10)
print(f"cible={cible}")

essai = int(input("votre proposition entre 1 et 10"))

if essai < 1 or essai > 10:
    print("erreur il faut saisir une valeur entre 1 et 10")
    exit()
if cible == essai:
    print("bravo")
elif cible < essai:
    print("trop élevé")
else :
    print("trop peu")
