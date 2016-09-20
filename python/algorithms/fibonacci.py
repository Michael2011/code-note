
"""
费波那契数列（意大利语：Successione di Fibonacci），又译费波拿契数、斐波那契数列、斐波那契数列、黄金分割数列。

在数学上，费波那契数列是以递归的方法来定义：

F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""

def fib1(n):
	if n in [0, 1]:
		return n
	
	else:
		return fib1(n-1) + fib1(n-2)
	


def fib2(n):
	a,b = 0, 1

	for i in range(n):
		a,b = b, a+b
	return a
