from factory import Factory, Faker, Sequence
"""Exemple de factory pour les membres."""
class MemberFactory(Factory):
    class Meta:
        model = dict

    id_membre = Sequence(lambda n: n + 1)
    id_geniALE = Sequence(lambda n: 100 + n)
    id_departement = Faker('random_int', min=1, max=10)
    date_admission = Faker('date_this_decade')