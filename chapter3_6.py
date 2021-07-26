# -*- coding: utf-8 -*-
#计算阶乘

def factorial(n):
	if n == 0 or n == 1:
		return 1

	total = 1
	for i in range(2,n+1):
			total = total *i
	return total

print(factorial(10))

