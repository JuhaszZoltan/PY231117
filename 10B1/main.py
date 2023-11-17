from module import *

print('Welcome n00b!')
lotto_tipus:int = lotto_tipus_bekerese()
tippek:list[int] = tippek_bekerese(lotto_tipus)
print(f'megjátszott számok: {tippek}')
nyeroszamok:list[int] = nyeroszamok_sorsolasa(lotto_tipus)
print(f'nyerőszámok:        {nyeroszamok}')
talalatok_szama:int = talalatszam_meghatarozasa(tippek, nyeroszamok)
print(f'találatok száma: {talalatok_szama}')