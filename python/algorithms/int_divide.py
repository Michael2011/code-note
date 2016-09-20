#!-*- coding:utf-8 -*-
"""
将一个整数，分拆为若干整数的和。例如实现： 4=3+1 4=2+2 4=2+1+1 4=1+1+1+1
"""

def int_divided(m,r,out_list):
    if(r==0):
        return True 

    tm = r
    while tm>0:
        if(tm<=m):
            out_list.append(tm)
            if(int_divided(tm,r-tm,out_list)):
                print out_list
            out_list.pop()
        tm = tm-1
    return False


n=6
out=[]
int_divided(n-1,n,out)
