
def f(x):
	return x**2

def newton(a, b, f, epsilon):
	x0 = (a+b)/2.0
	x = x0
	h = 1e-4
	while abs(f(x)) > epsilon:
		f_prime = (f(x+h) - f(x))/h
		x = x - f(x)/f_prime
	print("Le 0 se trouve en x =", x)
	print("En ce point, f(c) vaut :", f(x))

newton(-10, 10, f, 0.0001)