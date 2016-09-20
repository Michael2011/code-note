"""
快速排序，这是一个经典的算法，本文给出几种python的写法，供参考。

特别是python能用一句话实现快速排序。
"""

def qsort(lst):
	if not lst:
		return []

	else:
		less = [for i in lst if i < lst[0]]
		more = [for i in lst[1:] if i >= lst[0]]

		return qsort(less) + [lst[0]] + qsort(more)
		
