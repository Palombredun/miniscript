from math import cos, pi

def f(x):
    return cos(x)

def trapeze(f, a, b, n):
    total = (f(a) + f(b)) / 2
    step = (b - a) / n
    x = a + step
    for i in range(1, n):
        total += f(x)
        x += step

    print("Nombre de pas :", n)
    print("Longueur d'un pas :", step)
    print("Valeur de l'intégrale :", total*step)
    return total*step

trapeze(f, 0, pi, 100)