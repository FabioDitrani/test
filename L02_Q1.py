#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:48:40 2023

@author: fabioditrani
"""

import time
import numpy as np
from scipy.io import readsav
import scipy
from astropy.io import fits
import six.moves.cPickle as pickle
import matplotlib.pyplot as plt
import os
import yaml
import scipy.stats
from glob import glob
import sys
plt.style.use('default')
from scipy import interpolate
import itertools

#A
a = np.arange(1,16).reshape(3,5)
a = a.transpose()
print(a)
sliceo = np.array([1,3],dtype = int)
print(a[sliceo])
#B
array = np.ones([5,5])
array[1:-1,1:-1] = 0
print(array)