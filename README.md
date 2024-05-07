on peut former une chose ou une idée, et puis on peut la déformer, mais on ne peut pas lui enlever cette forme en l'_informant_ (la rendre informe). il faut inventer une autre verbe. je propose _informifier_ (pas parfait, mais libre). comme la quasi-totalité des _néoverbes_, _informifier_ est un verbe du premier groupe (comme probabiller ou exterpeler). à partir d'une seule de ses forme (par exemple _on informifie_), on doit alors pouvoir reconstruire son infinitif (et toutes les autres formes possibles). c'est le propos de ce module maladroit et imprécis mais qui parfois quand même fonctionne.

```python
import informifier

f = informifier.Informitif()

verbes = [
    "informifie",
    "informifions",
    "probabilliez",
    "exterpelait",
    "exterpelions",
    "hypercarraient",
]

f = Informitif()

for i in verbes:
    f(i)

('informifier', 'lancer')
('informifer', 'lancer')
('probabiller', 'lancer')
('exterpeler', 'jeter')
('exterpeler', 'jeter')
('hypercarrer', 'lancer')
# output: l'infinitif reconstitué et un verbe du même sous-groupe.
```
