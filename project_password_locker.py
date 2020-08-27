# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:52:41 2020

@author: George Chatzis
"""


passwords = {'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6','blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt','luggage': '12345'}
import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copyaccount password')
    sys.exit()