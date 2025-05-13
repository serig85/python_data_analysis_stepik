import pandas as pd


s ='7 11 3 5 10 12 11 9 6 1 8 11 1 4 9'.split(' ')
#s = '30 31 32 41 44 64'.split(' ')
si = map(int, s)
si = sorted(si)
print(si)
df = pd.DataFrame(data=si)
med = (list(df.median()))
print(f'Медиана {med[0]}')
print(f'Разброс {si[-1] - si[0]}')
