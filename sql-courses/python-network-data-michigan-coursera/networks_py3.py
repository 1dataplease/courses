# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:38:33 2017

@author: wainman
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os

os.getcwd()
os.chdir('C:\\Users\\wainman\\Desktop\\tw\\classes\\z online python-network-data was good no certificate')


#2-1
#regex getting started

#^ - beginning of line
#$ - end of line
#. - any character
#\s - whitespace
#\S - non-whitespace
#* - repeats a character 0 or more times
#*? - repeats a character 0 or more times, nongreedy, 1st one
#+ - repeats char 1 or more times
#+? - repeats char 1 or more times, nongreedy, stop at 1st
#[aeiou] - match a single char in the listed set
#[^XYZ] - match a single char not in the listed set
#[a-z0-9] the set of characters can include these ranges
#( - indicates where string extraction should start
#) - indicates where string extraction should end 

#see if string matches regEx Y/N
#re.search() - like str.find()

#extract portions of a string that match your regex
#like str.find and slicing
#re.findall()

#ex 1
handler = open('data/mbox-short.txt')
for line in handler:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

#5min