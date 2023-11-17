from random import randint

def lotto_tipus_bekerese() -> int:
    while True:
        tipus:str = input('milyen lottót szeretnél [5, 6, vagy 7]?: ')
        if tipus in ['5', '6', '7']:
            return int(tipus)
        else: print('ez nem lehetséges, válassz másikat!')


def tippek_bekerese(lt:int) -> list[int]:
    max:int = felso_hatarertek_maghatarozasa(lt)
    tippek:list[int] = []
    ssz:int = 1
    while len(tippek) < lt:
        szam:int = int(input(f'írd be az {ssz}. tipped: '))
        if szam < 1 or szam > max:
            print(f'a {szam} határértéken kívül esik, próbáld újra!')
        elif szam in tippek:
            print(f'a {szam} már volt, próbálj másikat!')
        else:
            tippek.append(szam)
            ssz += 1
    tippek.sort()
    return tippek

def nyeroszamok_sorsolasa(lt:int) -> list[int]:
    max:int = felso_hatarertek_maghatarozasa(lt)
    nyeroszamok:list[int] = []
    while len(nyeroszamok) < lt:
        szam:int = randint(1, max)
        if szam not in nyeroszamok:
            nyeroszamok.append(szam)
    nyeroszamok.sort()
    return nyeroszamok

def talalatszam_meghatarozasa(tippek:list[int], nyeroszamok:list[int]) -> int:
    talalatok_szama:int = 0
    for tipp in tippek:
        if tipp in nyeroszamok:
            talalatok_szama += 1
    return talalatok_szama

def felso_hatarertek_maghatarozasa(lt) -> int:
    if lt == 5: return 90
    if lt == 6: return 45
    if lt == 7: return 35