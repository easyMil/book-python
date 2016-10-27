
def parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


dane = range(0, 30)

parzyste1 = filter(parzysta, dane)
parzyste2 = filter(lambda x: x % 2 == 0, dane)
parzyste3 = filter(lambda x: not x % 2, dane)

#print(list(parzyste3))


def kwadrat(x):
    return pow(x, 2)


potegi1 = map(kwadrat, dane)
potegi2 = map(lambda x: pow(x, 2), dane)

#print(list(potegi1))


def opoznienie(przesuniecie):
    import datetime
    delay = pow(przesuniecie, 2)
    return datetime.datetime.now() + datetime.timedelta(seconds=delay)

czasy = map(opoznienie, dane)

#print(list(czasy))

from pprint import pprint
pprint(list(czasy))
