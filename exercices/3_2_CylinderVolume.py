# Exercice : Calculer le volume d'un cylindre
import math

# 1. Définir la valeur de Pi 
PI = math.pi 

# 2. Définir le rayon (r) et la hauteur (h) du cylindre
# Nous utilisons des 'float' (nombres décimaux)
r = 4.5  # Rayon en unités (ex: cm)
h = 10.0 # Hauteur en unités (ex: cm)

# 3. Calculer le volume
# La formule du volume d'un cylindre est V = π * r² * h
volume = PI * (r ** 2) * h 

# 4. Afficher le résultat
print(f"--- Calcul du volume d'un cylindre ---")
print(f"Rayon (r): {r}")
print(f"Hauteur (h): {h}")
print(f"Le volume du cylindre est : {volume:.2f} unités cubiques")