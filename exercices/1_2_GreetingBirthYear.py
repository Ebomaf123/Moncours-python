# Exercice : Salutation personnalisée et calcul de l'année de naissance
import datetime

# 1. Demander le nom de l'utilisateur
nom = input("Quel est votre nom ? ")

# 2. Demander l'âge
# Note: input() retourne toujours une chaîne de caractères, nous utilisons int() pour la convertir en nombre
try:
    age = int(input("Quel âge avez-vous ? "))
except ValueError:
    print("Veuillez entrer un nombre valide pour l'âge.")
    exit()

# 3. Calculer l'année de naissance
annee_courante = datetime.datetime.now().year
annee_naissance = annee_courante - age

# 4. Afficher le message personnalisé
print(f"Bonjour, {nom} ! Vous êtes né(e) aux alentours de l'année {annee_naissance}.")