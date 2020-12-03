import sys

arquivo = sys.argv[1]

xs = []
ys = []


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


try:
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
        teste = linhas[0].split
        for linha in linhas:
            w, z = linha.split(',')
            z = z.strip()
            x = float(w)
            y = float(z)
            xs.append(x)
            ys.append(y)
        print(Pearson(xs, ys))
except (ValueError, FloatingPointError):
    print("O valor informado não é um valor do tipo float!")
except ZeroDivisionError:
    print("Esta acontecendo divisão por 0!")
except FileNotFoundError:
    print("O arquivo texto informado não pode ser encontrado!")
except FileExistsError:
    print("O arquivo não existe!")
except IndexError:
    print("O arquivo está vazio!")
