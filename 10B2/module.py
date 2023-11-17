from random import randint

def lotto_tipus_bekerese() -> int:
    while True:
        lt:int = input('milyen lottót szeretnél játszani? ')
        if lt in ['5', '6', '7']:
            return int(lt)
        else: print('ez nem lehetséges, próbáld újra!')

def tippek_bekerese(lt:int) -> list[int]:
    max:int = felso_hatar_meghatarozasa(lt)
    tippek:list[int] = []
    ssz:int = 1
    while len(tippek) < lt:
        tipp:int = int(input(f'kérem az {ssz}. számot: '))
        if tipp < 1 or tipp > max:
            print('a tipp határértéken kívül esik, próbáld újra!')
        elif tipp in tippek:
            print('ez a szám már volt, próbálj egy másikat!')
        else:
            tippek.append(tipp)
            ssz += 1
    tippek.sort()
    return tippek


def nyeroszamok_huzasa(lt:int) -> list[int]:
    max:int = felso_hatar_meghatarozasa(lt)
    nyeroszamok:list[int] = []
    while len(nyeroszamok) < lt:
        szam:int = randint(1, max)
        if szam not in nyeroszamok:
            nyeroszamok.append(szam)
    nyeroszamok.sort()
    return nyeroszamok

def talalatok_szamanak_meghatarozasa(tippek:list[int], nyeroszamok:list[int]) -> int:
    talalatok_szama:int = 0
    for tipp in tippek:
        if tipp in nyeroszamok:
            talalatok_szama+= 1
    return talalatok_szama

def felso_hatar_meghatarozasa(lt:int) -> int:
    if lt == 5: return 90
    elif lt == 6: return 45
    elif lt == 7: return 35