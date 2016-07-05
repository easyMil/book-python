from django.db import models


class Adres(models.Model):
    kontakt = models.ForeignKey('kontakt.Kontakt')
    ulica = models.CharField(max_length=50)
    nr_domu = models.CharField(max_length=5)
    nr_mieszkania = models.CharField(max_length=5, blank=True, null=True)
    miejscowosc = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=50)


class Kontakt(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=50, db_index=True)
    telefon = models.IntegerField(db_index=True)
    zdjecie = models.FileField(blank=True, null=True)
    data_urodzenia = models.DateField()
    komentarz = models.TextField(blank=True, null=True)
    jest_adminem = models.BooleanField()

    def __str__(self):
        return '{imie} {nazwisko}'.format(
            imie=self.imie,
            nazwisko=self.nazwisko,
        )