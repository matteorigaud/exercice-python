// exo 6.15
// Trouvez la chaîne de caractères la plus longue dans une liste.
// Affichez son index, sa valeur et sa longueur.
//
// ATTENTION : ne pas utiliser la fonction list.index()
// ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

// réponse 6.15

// my_list,length
// my_list[0].length

let index = null;
let valeur = " ";
let longueur = 0;

for (let i = 0; i < my_list.length; i++) {
    // console.log(i);
    // console.log(my_list[i]);
    // console.log(my_list[i].length);
    // console.log();

    let prop = my_list[i];

    if (my_list[i].length > longueur) {
    // mise à jour, c-à-d stockage de la plus grande longueur rencontrée jusque maintenant
    longueur = my_list[i].length;
    // stockage des autres informations demandée
    index = 1;
    valeur = my_list[i];

    }
}