# exo 4.2
# écrivez un bloc if qui affiche
# - "le nombre est pair" si le modulo par 2 de la variable number est égal à zéro
# - "le nombre est impair" si le modulo par 2 de la variable number n'est pas égal à zéro

import random

# affectaction d'un nombre entier entre 0 et 9 à la variable number
number = random.randint(0, 9)
print(number)

# réponse 4.2

import random

number = random.randint(0, 9)
print(number)

if number % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")
