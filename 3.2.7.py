def my_cov():
    mxy =([2, 3], [10, 4], [5, 7], [4, 11], [7, 2], [7, 11], [1, 11],
          [4, 8], [7, 8], [8, 1], [6, 2], [6, 2], [6, 8], [7, 5], [10, 9])

    lmxy = len(mxy)
    sx = 0
    sy = 0
    sxy = 0

    for i in mxy:
        sxy += i[0]*i[1]
        sx += i[0]
        sy += i[1]
    xy = sxy/lmxy
    x = sx/lmxy
    y = sy/lmxy
    return (xy - x*y)


import pandas as pd

df = pd.DataFrame([(2, 3), (10, 4), (5, 7), (4, 11), (7, 2),(7, 11),(1, 11),(4, 8),(7, 8),(8, 1),(6, 2),(6, 2),(6, 8),(7, 5),(10, 9)],
                  columns=['x', 'y'])
print(f'Реализация пандас {df.cov()}')

print(f'Моя реализация по курсу {my_cov()}')
