# exo 6.12
# Comptez les nombres plus petits ou égaux à 10 dans la liste et affichez le résultat
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.12

my_list = [2.71, 42, 123, 2, 3.14, 1.61]
count = 0

for number in my_list:
    if number <= 10:
        count += 1

print("Nombre de nombres <= 10 :", count)
