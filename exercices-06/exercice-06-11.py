# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
# Note : faites une boucle et n'utilisez pas la méthode `index()`
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11

my_list = [2.71, 42, 123, 2, 3.14, 1.61]
target_value = 3.14
index = None

for i in range(len(my_list)):
    if my_list[i] == target_value:
        index = i
        break

print("Index de la valeur 3.14 :", index)
