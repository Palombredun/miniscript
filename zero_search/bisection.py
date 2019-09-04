
def f(x):
	return x +2

def bisection(a, b, f, epsilon):
	m = (a+b)/2.0
	while abs(f(m)) > epsilon:
		if f(a)*f(m) < 0:
			b = m
		elif f(b)*f(m) < 0:
			a = m
		m = (a+b)/2.0
	print("Le 0 se trouve en x =", m)
	print("En ce point, f(c) vaut :", f(m))

bisection(-10, 10, f, 0.0001)