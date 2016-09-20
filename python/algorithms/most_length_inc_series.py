arr1 = [1,3,5,2,4,6,7,8]
arr2 = [1,2,4,6,7,8]
arr3 = [89, 256, 78, 1, 46, 78, 8]

def most_length_inc_series(lst):
	if len(lst) <= 1:
		return len(lst), lst

	cdr = [i for i in lst if i > lst[0]]	
	
	sub_len1, sub_lst1 = most_length_inc_series(lst[1:])
	sub_len2, sub_lst2 = most_length_inc_series(cdr)

	if sub_len1 > sub_len2 + 1:
		return sub_len1, sub_lst1
	else:
		return sub_len2 + 1, [lst[0]] + sub_lst2

print most_length_inc_series(arr1)
print most_length_inc_series(arr2)
print most_length_inc_series(arr3)


