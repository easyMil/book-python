#!/usr/bin/env python3

from pprint import pprint
import sys


def czytaj_passwd():
    with open('/etc/passwd') as file:

        for linia in file.readlines():
            if not linia.startswith('#'):
                yield linia


zawartosc = czytaj_passwd()

#print(sys.getsizeof(zawartosc))
#print(list(zawartosc))
#sys.exit()






def czytaj_passwd_tradycyjnie():
    with open('/etc/passwd') as file:
        tresc_pliku = []

        for linia in file.readlines():
            if not linia.startswith('#'):
                return linia
                tresc_pliku.append(linia)

        return tresc_pliku


zawartosc_tradycyjna = czytaj_passwd_tradycyjnie()

#print(zawartosc_tradycyjna)

print(sys.getsizeof(zawartosc_tradycyjna))