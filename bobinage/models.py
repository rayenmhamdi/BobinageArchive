from django.db import models

# Create your models here.


class Archive(models.Model):
    marque = models.CharField(max_length=120, null=False, blank=False)
    CHEVEAUX_CHOICES = zip(range(1, 21), range(1, 21))
    Cheveaux = models.IntegerField(choices=CHEVEAUX_CHOICES, blank=False, null=False)
    TYPE_CHOICES = (
        ('Monophasé', 'Monophasé'),
        ('Triphasé', 'Triphasé')
    )
    type = models.CharField(max_length=120, choices=TYPE_CHOICES, blank=False, null=False)
    Amperage = models.PositiveIntegerField(blank=False, null=False)
    COUPLAGE_CHOICES = (
        ('Parallèle Etoile', 'Parallèle Etoile'),
        ('Parallèle Triangle', 'Parallèle Triangle'),
        ('Serie Etoile', 'Serie Etoile'),
        ('Serie Triangle', 'Serie Triangle')
    )
    couplage = models.CharField(max_length=120, choices=COUPLAGE_CHOICES, blank=False, null=False)
    nb_spire_principale =  models.PositiveIntegerField(blank=False, null=False)
    nb_spire_aux = models.PositiveIntegerField(blank=True, null=True)
    longeur_rotor_mm = models.PositiveIntegerField(blank=False, null=False)
    diametre_rotor_mm = models.PositiveIntegerField(blank=False, null=False)