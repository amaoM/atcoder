# coding: utf-8

if __name__ == '__main__':
	N = int(input())
	
	d = 2025 - N

	for i in range(1, 10):

		if d % i == 0 and 9 >= d // i:
			print('{:d} x {:d}'.format(i, d // i))