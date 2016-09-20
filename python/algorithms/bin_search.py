

def binarysearch(lst, value, low, high):
	if high < low:
		return -1

	if not lst:
		return -1

	mid = (low + high) / 2
	if lst[mid] > value:
		return binarysearch(lst[:mid], value, low, mid-1)

	elif lst[mid] < value:
		return binarysearch(lst[mid:], value, low+1, high)
	
	else:
		return mid


def binarysearch2(lst, value, low, high):
	if high < low:
		return -1

	if not lst:
		return -1
	

	mid = (low + high) / 2
	while low <= high:
		if lst[low] < value:
			low = mid + 1

		elif lst[low] > value:
			high = mid - 1

		else:
			return mid

	return -1

