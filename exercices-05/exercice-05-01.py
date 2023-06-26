# exo 5.1
# Ajoutez de la documentation à la fonction suivante et vérifiez
# qu'elle s'affiche correctement en utilisant la fonction help()

# réponse 5.1

def multiplication(a: float, b: float) -> float:
    return a * b


def multiplication(a: float, b: float) -> float:
    """
    Cette fonction effectue la multiplication de deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: Le résultat de la multiplication.

    """
    return a * b
