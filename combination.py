#!/usr/bin/python
#-*- coding: utf-8 -*-

def all_combination(n,k):
	if k == 1:
		li = map(lambda m: [m],range(n))
		return li;
	else:
		li = all_combination(n,k-1)
		new_li = list()
		for t_l in li:
			for t_k in range(n):
				if (t_k in t_l) == False:
					tmp_l = list(t_l)
					tmp_l.append(t_k)
					new_li.append(tmp_l)
		return new_li
		
print all_combination(4,3)
