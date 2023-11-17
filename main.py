from module import *

print('W3lc0m3 N00b!')

lotto_tipus:int = lotto_tipus_bekerese()
tippek:list[int] = tippek_bekerese(lotto_tipus)
print(f'tippek: {tippek}')
nyeroszamok:list[int] = nyeroszamok_huzasa(lotto_tipus)
print(f'nyerőszámok: {nyeroszamok}')
talalat:int = talalatok_szamanak_meghatarozasa(tippek, nyeroszamok)
print(f'találatok száma: {talalat}')