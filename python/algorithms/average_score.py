"""
/********************************************************
*   Copyright (C) 2016 All rights reserved.
*   
*   Filename:average_score.py
*   Author  :luoyingbo#fotoable.com
*   Date    :2016-09-20
*   Describe:
"""

def less_average(score):
	num 	  = len(score)
	sum_score = sum(score)

	average = sum_score / num

	less_average = [i for i in score if i < average
	
	return len(less_average)
