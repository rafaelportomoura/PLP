import sys

arquivo = sys.argv[1]

xs = []
ys = []

with open(arquivo, 'r') as file:
    linhas = file.readlines()
    for linha in linhas:
        x, y = linha.split(',')

        xs.append(float(x))
        ys.append(float(y.strip()))


def somatorio(num, tam):
    soma = 0
    for i in range(tam):
        soma += num[i]
    return soma


def barCalc(num, tam, pos):
    return 1/tam * somatorio(num, tam)


def denominador(x, y):
    z = []
    tam = len(x)
    for pos in range(tam):
        z.append((x[pos] - barCalc(x, tam, pos))
                 * (y[pos] - barCalc(y, tam, pos)))
    return sum(z)


def numerador(x, y):
    zx = []
    zy = []
    tam = len(x)
    for pos in range(tam):
        x2 = pow(x[pos] - barCalc(x, tam, pos), 2)
        y2 = pow(y[pos] - barCalc(y, tam, pos), 2)
        zx.append(x2)
        zy.append(y2)
    return pow((sum(zx)*sum(zy)), 0.5)


def Pearson(x, y):
    return denominador(x, y) / numerador(x, y)


print(Pearson(xs, ys))
