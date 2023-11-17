from module import *

lotto_tipus:int = 0

print('Welcome n00b!')
lotto_tipus = lt_beker()
tippek:list[int] = tippek_bekerese(lotto_tipus)
print(f'tippek:      {tippek}')
nyeroszamok:list[int] = nyeroszamok_generalasa(lotto_tipus)
print(f'nyerőszámok: {nyeroszamok}')
print('-------------')
talalatok:int = talalatok_szama(tippek, nyeroszamok)
print(f'találatok száma: {talalatok}')