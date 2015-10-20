#!/usr/bin/python
#-*- coding: utf-8 -*-

def all_ordered_combination(n,k):
	if k == 1:
		li = map(lambda m: [m],range(n))
		return li;
	else:
		li = all_ordered_combination(n,k-1)
		new_li = list()
		for t_l in li:
			for t_k in range(n):
				if (t_k in t_l) == False:
					tmp_l = list(t_l)
					tmp_l.append(t_k)
					new_li.append(tmp_l)
		return new_li

def all_combination(n,k):
	if k == 0:
		return [[]]
	elif n == k:
		return [range(0,n)]
	else:
		li = all_combination(n-1,k)
		li2 = all_combination(n-1,k-1)
		li2 = map(lambda e: e+[n-1] ,li2)
		return li+li2
		
print all_combination(4,1)
