import re
from informifier.terminaisons import TERM_PREMIER_GROUPE


terms = r"|".join(TERM_PREMIER_GROUPE)
re_term = re.compile(rf"({terms})$")

# deux listes utiles pour essayer de distinguer entre les verbes en -e<consonne>er et -é<consonne>er, même si c'est loin d'être parfait.
e_consonne = [
    "c",
    "d",
    "g",
    "m",
    "n",
    "p",
    "r",
    "s",
    "v",
    "vr",
]
# fmt: off
eaigu_consonne = [
    "b", "br", "c", "ch", "cr", "d", "fl", "g", "gl", 
    "gn", "gr", "gu", "j", "l", "m", "n", "p", "qu", 
    "r", "s", "t", "tr", "v", "vr",
]
# fmt: on
eaigu_consonne = r"|".join(eaigu_consonne)
e_consonne = r"|".join(e_consonne)

# compile les regexes
re_c = re.compile("(ç|c)$")  # cer
re_g = re.compile("ge?$")  # ger
re_eler = re.compile("(èl|ell?)$")  # eler
re_eter = re.compile("(èt|ett?)$")  # eter
re_y = re.compile("y$")  # yer
re_voyellei = re.compile("([aou])i$")  # [aou]yer
re_eaiguer = re.compile(rf"[èé]({eaigu_consonne})$")
re_econsonneer = re.compile(rf"[eè]({e_consonne})$")

RULES = [
    (re_c, "cer", "lancer"),
    (re_g, "ger", "lancer"),
    (re_voyellei, r"\1yer", "lancer"),
    (re_y, "yer", "lancer"),
    (re_eler, "eler", "jeter"),
    (re_eter, "eter", "jeter"),
    (re_eaiguer, r"é\1er", "sécher"),
    (re_econsonneer, r"e\1er", "sécher"),
]
