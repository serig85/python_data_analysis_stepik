

mass = (2, 8, 10, 3, 1, 8, 6, 9, 11, 1)


def viborochnoe_sredn(mass):
    return(sum(mass)/len(mass))



def std_otkl(mass):
    d =[]
    vs = viborochnoe_sredn(mass)
    for i in mass:
        d.append((i-vs)**2)
    sd = sum(d)

    return (round((sd/(len(mass)-1))**0.5, 1))

print(f'Выборочное среднее {viborochnoe_sredn(mass)}')
print(f'Стандартное отклонение {std_otkl(mass)}')
