import re

test_verbs = [
    "informifie",
    "informifions",
    "hyperifierais",
    "probabilliez",
    "marouflaient",
    "exterpelait",
]

verb = test_verbs[2]

# il faut faire par étape.
# quels sont les différents sous-groupes des verbes du premier groupe, et comment les reconnaître?
#

# plusieurs groupes d'exceptions qui modifie le radical:
# verbes en -cer.
# verbes en -ger.
# verbes en -e<consonne>-er (1)
# verbes en -e<consonne>-er (2)
# verbes en -é<consonne(s)>-er
# verbes en -yer
# verbes en -ayer
# verbes en -oyer
# verbes en -eyer
# verbe envoyer et dérivés, encore une exception.


# les verbes en -cer et -ger, on ajoute un -e ou on remplace c par ç avant un "o" ou un "a".

# if verbe_ger(verb): # ex. manger
#     # ge(ai[st]|aient|ons|ont)
#     infinitif = re.sub(terminaison, "ger", verb)
#     like = "manger"
# elif verbe_cer(verb): # ex. lancer
#     # en soi, je peux aussi simplement enlever le "e" et m'en ficher?
#     infinitif = re.sub()
#     like = "lancer"
# elif verbe_e_consonne_1(verb):
#     ...
# elif verbe_e_consonne_2(verb):
#     ...
# elif verb_eaigu_consonne(verb):
#     ...
# elif verbe_yer(verb):
#     ...
# elif verbe_ayer(verb):
#     ...
# elif verbe_oyer(verb):
#     ...
# elif verbe_eyer(verb):
#     ...

terminaisons = set(
    [
        # 1) indicatif
        # 1.1) présent
        ["e", "es", "e", "ons", "ez", "ent"]
        # 1.2) imparfait
        + ["ais", "ais", "ait", "ions", "iez", "aient"]
        # 1.3) futur simple
        + ["erai", "eras", "era", "erons", "erez", "eront"]
        # 1.4) passé simple
        + ["ai", "as", "a", "âmes", "âtes", "èrent"]
        # 1.5) passé composé
        + ["é", "é", "é", "é", "é", "é", "é"]
        # 2) subjonctif
        # 2.1) présent
        + ["e", "es", "e", "ions", "iez", "ent"]
        # 2.2) imparfait
        + ["asse", "asses", "ât", "assions", "assiez", "assent"]
        # 3) conditionnel
        # 3.1) présent
        + ["erais", "erais", "erait", "erions", "eriez", "eraient"]
        # 4) impératif
        # 4.1) présent
        + ["e", "ons", "ez"]
        # 5) participe
        # 5.1) présent
        + ["ant"]
        # 5.2) passé
        + ["é", "és", "ée", "ées"]
    ][0]
)

# pour obtenir les terminaisons en [ao], qui requièrent un traitement particulier pour certains verbes, il suffit de regarder la première lettre.
terminaison_ao = {i for i in set(terminaisons) if i[0] in ("a", "â", "o")}
terminaison_pas_ao = terminaisons - terminaison_ao

# je vérifie que tout est là:
print(len(terminaisons) - len(terminaison_ao) - len(terminaison_pas_ao))

verbe_en_ger = rf"ge({r'|'.join(terminaison_ao)})$|g({r'|'.join(terminaison_pas_ao)})$"

verbe_en_cer = rf"ç({r'|'.join(terminaison_ao)})$|c({r'|'.join(terminaison_pas_ao)})$"


re.sub(verbe_en_cer, "cer", 'lançons')

for i in ["lancer", "lançons", "lancez", "lance", "lanceraient", "lançais", "lançaient"]:
    print(i, re.sub(verbe_en_cer, "cer", i))

for i in ["mangeais", "mangions", "mangerons", "mangerions", "mangeant"]:
    print(i, re.sub(verbe_en_ger, "ger", i))


