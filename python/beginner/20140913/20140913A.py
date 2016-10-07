# coding: utf-8

def inspection(sweets, number):

	if sweets > number:
		print(number - sweets % number)

	else:
		print(number - sweets)

if __name__ == '__main__':
	args = []

	for i in range(2):
		args.append(int(input()))

	inspection(args[0], args[1])