from math import cos, pi

def f(x):
	return cos(x)

def simpson(f, a, b, n):
	step = (b-a)/n
	x = a
	# intégrale = delta/3*( (f(x0)+f(xn))/2 + 2*f(x1/2) + sum(f(xk) + 2*f(x1/2)))
	total = (f(a) + f(b))/2 + 2 * f((a + step)/2)
	for i in range(1, n):
		total += f(x) + 2*f(x + step/2)
		x += step
	print("Nombre de pas :", n)
	print("Longueur d'un pas :", step)
	print("Valeur de l'intégrale :", total*step/3)
	return total * step/3

simpson(f, 0, pi, 100)