# exo 3.6
# La formule suivante permet de convertir des « miles » en mètres :
#
# miles * 1609.344 = mètres
#
# Bob est en Angleterre.
# On lui dit que la boulangerie la plus proche est à 3 miles.
# Calculez la distance en mètres avec la variable `miles` puis stockez le résultat dans la variable `meters`.
# Affichez un résultat arrondi de la distance en mètres avec la fonction `round()`.
# Convertissez les mètres en kilo mètres puis stockez le résultat dans la variable `km`.
# Affichez un résultat arrondi de la distance en kilo mètre avec la fonction `round()`.

miles = 3

# réponse 3.6

miles = 3
meters = miles * 1609.344
rounded_meters = round(meters)
km = meters / 1000
rounded_km = round(km)

print("Distance en mètres :", rounded_meters)
print("Distance en kilomètres :", rounded_km)

