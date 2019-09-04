import sys

import matplotlib.pyplot as plt

from app.projectile import Projectile
from app.constants import *
from app.units import *


proj = Projectile()

arg_names = ['command', 'exp']
args = dict(zip(arg_names, sys.argv))

if not args['exp']:
    print("Tapez python main.py help pour afficher l'aide")

if args['exp'] == 'help':
    print("Tapez 'exp1' pour lancer un projectile avec un angle de 45 degrés sans frottements ni vent.")
    print("Tapez 'exp2' pour lancer un projectile avec un angle variant entre 30 et 60 degrés, sans frottements ni vent.")
    print("Tapez 'exp3' pour lancer un projectile avec un angle de 45 degrés avec des frottements (de la forme k*v sans vent.")
    print("Tapez 'exp4' pour lancer un projectile avec un angle de 45 degrés sans frottements mais avec des bourrasques de vent contraire aléatoires.")
elif args['exp'] == 'exp1':
    intervall, y_values = proj.basic_throw()
    print(intervall)
    for i in range(30):
        intervall, y_values = proj.throw_random_angle()
        plt.plot(intervall, y_values)
        plt.ylim(0, 10)
        plt.xlim(0, 10)
elif args['exp'] == 'exp2':
    intervall, y_values = proj.throw_random_angle()

plt.show()