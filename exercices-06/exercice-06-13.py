# exo 6.13
# Multipliez chacun des nombres dans la liste par 100, réaffactez le résultat à la place de la valeur originelle puis affichez le résultat
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

for i in range(len(my_list)):
    my_list[i] = my_list[i] * 100

print("Liste après multiplication par 100 :", my_list)
