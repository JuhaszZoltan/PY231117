from random import randint

def lt_bekeres() -> int:
    while True:
        lt:str = input('Milyen típusú lottót szeretnél játszani (5, 6 vagy 7)? ')
        if lt in ['5', '6', '7']: return int(lt)
        else: print('Ez nem lehetséges, próbáld újra!')


def t_bekeres(lt:int) -> list[int]:
    max_szam:int = max_meghat(lt)
    tippek:list[int] = []
    ssz:int = 1
    while len(tippek) < lt:
        t:int = int(input(f'írd be az {ssz}. tippet: '))
        if t in tippek:
            print('ez már volt, próbáld újra!')
        elif t < 1 or t > max_szam:
            print('határértéken kívül van, próbáld újra!')
        else:
            tippek.append(t)
            ssz += 1
    tippek.sort()
    return tippek


def ny_generalas(lt:int) -> list[int]:
    max_szam:int = max_meghat(lt)
    nyeroszamok:list[int] = []
    while len(nyeroszamok) < lt:
        szam:int = randint(1, max_szam)
        if szam not in nyeroszamok:
            nyeroszamok.append(szam)
    nyeroszamok.sort()
    return nyeroszamok


def tal_szama(t:list[int], ny:list[int]) -> int:
    talalat:int = 0
    for szam in t:
        if szam in ny:
            talalat += 1
    return talalat


def max_meghat(lt:int) -> int:
    if lt == 5: return 90
    if lt == 6: return 45
    if lt == 7: return 35