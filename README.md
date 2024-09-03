informifier
===========

On peut former une chose ou une idée, et puis on peut la déformer, mais on ne peut pas lui enlever cette forme en l'_informant_ (la rendre informe). il faut inventer un autre verbe. Je propose _informifier_ (pas parfait, mais libre). Comme la quasi-totalité des _néoverbes_, _informifier_ est un verbe du premier groupe (comme probabiller ou exterpeler). À partir d'une seule de ses formes (par exemple _on informifie_), on doit alors pouvoir reconstruire son infinitif (et toutes les autres formes possibles). C'est le propos de ce module maladroit et imprécis mais qui parfois quand même fonctionne.

```python
import informifier

verbes = [
    "informifie",
    "informifions",
    "probabilliez",
    "exterpelait",
    "exterpelions",
    "hypercarraient",
]

for i in verbes:
    informifier.informifier(i)

('informifier', 'lancer')
('informifer', 'lancer')
('probabiller', 'lancer')
('exterpeler', 'jeter')
('exterpeler', 'jeter')
('hypercarrer', 'lancer')
# l'output est l'infinitif reconstitué
# et un verbe du même sous-groupe.
```
