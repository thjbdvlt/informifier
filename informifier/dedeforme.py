from informifier.patterns import RULES, re_term


def raciner(verb):
    """Enlève la terminaison d'un verbe du premier groupe.

    Args:
        verb (str):  le verbe, conjugué ou non.

    Returns (str):  la racine du verbe.
    """

    return re_term.sub("", verb)


def _infinitiver(verb_stem):
    """Refaire l'infinitif et trouver un verbe modèle.

    Args:
        verb_stem (str):  la racine du verbe.

    Returns (tuple):  l'infinitif du verbe et un verbe du même groupe.
    """

    for pattern, term, group in RULES:
        if pattern.search(verb_stem):
            return pattern.sub(term, verb_stem), group
    return verb_stem + "er", "lancer"  # par défaut: lancer


def informifier(verb):
    """Racine, infinitive et trouve le modèle.

    Args:
        verb (str):  le verbe conjugué ou non.

    Returns (tuple):  l'infinitif du verbe et un verbe du même groupe.
    """

    stem = raciner(verb)
    inf, group = _infinitiver(stem)
    return inf, group
