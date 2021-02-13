from django.db import models

# Create your models here.
class Debitor(models.Model):

    name = models.CharField(max_length=300, null=True, blank=True)
    vorname = models.CharField(max_length=300, null=True, blank=True)
    strasse = models.CharField(max_length=300, null=True, blank=True)
    hausnummer = models.CharField(max_length=300, null=True, blank=True)
    plz = models.CharField(max_length=300, null=True, blank=True)
    ort = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.name, self.vorname)



class Kreditor(models.Model):

    firma = models.CharField(max_length=300, null=True, blank=True)
    strasse = models.CharField(max_length=300, null=True, blank=True)
    hausnummer = models.CharField(max_length=300, null=True, blank=True)
    plz = models.CharField(max_length=300, null=True, blank=True)
    ort = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.firma



class Ausgangsrechnung(models.Model):

    ARTS = (('Dienstleistung','Dienstleistung'), ('Produkt','Produkt'))
    STATS = (('Offen','Offen'), ('Bezahlt','Bezahlt'))

    debitor = models.ForeignKey(Debitor, null=True, on_delete=models.CASCADE, blank=True)
    art = models.CharField(max_length=300, choices=ARTS, null=True, blank=True)
    beschreibung = models.CharField(max_length=300, null=True, blank=True)
    preis = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=300, choices=STATS, null=True, blank=True)
    datum = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'id: %s | für %s am %s' % (self.id, self.debitor, self.datum.date())


class Eingangsrechnung(models.Model):

    ARTS = (('Dienstleistung','Dienstleistung'), ('Produkt','Produkt'))
    STATS = (('Offen','Offen'), ('Bezahlt','Bezahlt'))

    kreditor = models.ForeignKey(Kreditor, null=True, on_delete=models.CASCADE, blank=True)
    art = models.CharField(max_length=300, choices=ARTS, null=True, blank=True)
    beschreibung = models.CharField(max_length=300, null=True, blank=True)
    preis = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=300, choices=STATS, null=True, blank=True)
    datum = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'id: %s | für %s am %s' % (self.id, self.kreditor, self.datum.date())
