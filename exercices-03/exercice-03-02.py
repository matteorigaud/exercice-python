# exo 3.2
# Bob veut distribuer tous ses bonbons et chocolats à ses amis.
# Il a 15 bonbons, 17 chocolats et 3 amis.
# Combien de bonbons lui restera-t-il ?
# Calculez le reste de bonbons puis stockez le résultat dans la variable `candies_rest`.
# Combien de chocolats lui restera-t-il ?
# Calculez le reste de chocolats puis stockez le résultat dans la variable `chocolates_rest`.
# Affichez ces résultats.

candies = 15
chocolates = 17
friends = 3

# réponse 3.2

candies_per_friend = candies // friends
candies_rest = candies - (candies_per_friend * friends)

chocolates_per_friend = chocolates // friends
chocolates_rest = chocolates - (chocolates_per_friend * friends)

print("Bonbons restants :", candies_rest)
print("Chocolats restants :", chocolates_rest)
