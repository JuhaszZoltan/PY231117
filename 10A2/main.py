from module import *

print('w3lc0m3 n00b!')
lotto_tipus:int = lt_bekeres()
tippek:list[int] = t_bekeres(lotto_tipus)
print(f'tippek: {tippek}')
nyeroszamok:list[int] = ny_generalas(lotto_tipus)
print(f'nyerőszámok: {nyeroszamok}')
talalatok:int = tal_szama(tippek, nyeroszamok)
print(f'találatok száma: {talalatok}')