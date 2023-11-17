from random import *

def tippek_bekerese(lotto_tipus:int) -> list[int]:
    max_szam:int = max_meghatarozasa(lotto_tipus)
    tippek:list[int] = []
    szamlalo:int = 1
    while len(tippek) < lotto_tipus:
        tipp:int = int(input(f'add meg az {szamlalo}. tippet: '))
        if tipp < 0 or tipp > max_szam:
            print('a tipp nincs a határértéken belül!')
        elif tipp in tippek:
            print('ez a szám már volt!')
        else:
            tippek.append(tipp)
            szamlalo += 1
    tippek.sort()
    return tippek


def nyeroszamok_generalasa(lotto_tipus:int) -> list[int]:
    max_szam:int = max_meghatarozasa(lotto_tipus)
    nyeroszamok:list[int] = []
    while len(nyeroszamok) < lotto_tipus:
        nysz:int = randint(1, max_szam)
        if nysz not in nyeroszamok:
            nyeroszamok.append(nysz)
    nyeroszamok.sort()
    return nyeroszamok


def talalatok_szama(tippek:list[int], nyeroszamok:list[int]) -> int:
    talalat:int = 0
    for nysz in nyeroszamok:
        if nysz in tippek:
            talalat += 1
    return talalat


def max_meghatarozasa(lotto_tipus:int) -> int:
    if lotto_tipus == 5: return 90
    elif lotto_tipus == 6: return 45
    elif lotto_tipus == 7: return 35


def lt_beker() -> int:
    lt:int = 0
    while True:
        lt = int(input('Milyen lottót szeretnél játszani [5, 6 vagy 7]? '))
        if lt not in [5, 6, 7]: print('ilyen lottó nincs! próbáld újra!')
        else: return lt