# coding: utf-8

def inspection(products, prices):
	binary = format(int(products[1]), 'b')
	result = 0

	for b in range(len(binary), 0, -1):
		
		if binary[-b] == '1':
			result += int(prices[b - 1])

	print(result)
	return True

if __name__ == '__main__':
	args = []

	for i in range(2):
		v = input()
		args.append(v)

	inspection(args[0].split(' '), args[1].split(' '))