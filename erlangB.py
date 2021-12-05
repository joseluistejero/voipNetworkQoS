#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@reprository: https://github.com/diegodafranca/erlangB
"""

#Erlang B Calculator
from math import ceil

#this function returns the probability of not answering a call given the BHC Volume in Erlangs (p) and c the number of phone lines 
def probability(p,c):
  if(p == 0):
    return 0.0
  s= 0.0
  for i in range(1,c):
    s = (1.0 + s)*(i/p)
  pc = 1.0/(1.0 + s)
  return pc

#this function returns the number of lines given certain values of p and prob, where p is the BHC Volume in Erlangs and prob the probability of not answering a call 
def lines(p,prob):
  l,r = 0,ceil(p)
  fR = probability(p,r)
  while(fR > prob):
    l = r
    r = r + 32
    fR = probability(p,r)
  while(r-l)>1:
    mid = ceil((l+r)/2)
    fMid = probability(p,mid)
    if fMid > prob:
      l = mid
    else:
      r = mid
  return r - 1

