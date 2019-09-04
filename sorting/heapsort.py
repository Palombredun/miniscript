import random

import pdb

array = [random.randint(0,10) for i in range(10)]

def heapify(tree, node, n):
	k = node
	j = 2*k
	#pdb.set_trace()
	while j <= n:
		if j < n and tree[j] < tree[j+1]:
			j += 1
		if tree[k] < tree[j]:
			tree[k], tree[j] = tree[j], tree[k]
			k = j
			j = 2*k
		else:
			j = n+1

def heapsort(tree, length):
	for i in range(length//2, 1, -1):
		heapify(tree, i, length)
	for i in range(length, 1, -1):
		tree[i], tree[1] = tree[1], tree[i]
		heapify(tree, 1, i-1)

print(array)
heapsort(array, len(array)-1)
print(array)