import sys
import collections

def main():
	arg_names = ['command', 'exp']
	args = dict(zip(arg_names, sys.argv))
	if args['exp'] == 'exp1':
		print('exp1')
	elif args['exp'] == 'exp2':
		print('exp2')

if __name__ == '__main__':
  main()