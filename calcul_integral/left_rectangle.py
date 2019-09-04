from math import cos, pi

def f(x):
	return cos(x)

def left_rectangle(f, a, b, n):
	total = 0
	step = (b - a)/n
	x = a
	for i in range(0, n):
		total += f(x)
		x += step
	print("Nombre de pas :", n)
	print("Longueur d'un pas :", step)
	print("Valeur de l'intégrale :", total*step)
	return total*step

left_rectangle(f, 0, pi, 100)