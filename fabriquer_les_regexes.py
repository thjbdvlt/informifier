import re


test_verbs = [
    "informifie",
    "informifions",
    "hyperifierais",
    "probabilliez",
    "marouflaient",
    "exterpelait",
]


class Informitif:
    """cherche l'infinitif d'un verbe du premier groupe."""
    term = set([
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
    ][0])

    def __init__(self):
        """initie un objet pour trouver l'infinitif de verbes."""

        t = r"|".join(self.term)
        x = fr"({t})$"
        self.re_term = re.compile(x)

        # deux listes utiles pour essayer de distinguer entre les verbes en -e<consonne>er et -é<consonne>er, même si c'est loin d'être parfait.
        e_consonne = ["c", "d", "g", "m", "n", "p", "r", "s", "v", "vr"]
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
        self.re_c = re.compile("(ç|c)$")  # cer
        self.re_g = re.compile("ge?$")  # ger
        self.re_eler = re.compile("(èl|ell?)$")  # eler
        self.re_eter = re.compile("(èt|ett?)$")  # eter
        self.re_iy = re.compile("[yi]$")  # yer
        self.re_eaiguer = re.compile(rf"[èé]({eaigu_consonne})$")
        self.re_econsonneer = re.compile(rf"[eè]({e_consonne})$")

        self.rules = [
            (self.re_c, "cer", "lancer"),
            (self.re_g, "ger", "lancer"),
            (self.re_iy, "yer", "lancer")
            (self.re_eler, "eler", "jeter"),
            (self.re_eter, "eter", "jeter"),
            (self.re_eaiguer, r"é\1", "sécher"),
            (self.re_econsonneer, r"e\1", "sécher"),
        ]

        def raciner(verb):
            """enlève la terminaison d'un verbe du premier groupe."""

            return self.re_term.sub("", verb)

        def infinitiver(self, verb):
            for pattern, term, group in self.rules:
                if pattern.search(verb):
                    return pattern.sub(term, verb), group
            return verb + "er", "lancer"

        def __call__(self, verb):
            stem = self.raciner(verb)
            inf, group = self.infinitiver(stem)
            return inf, group
