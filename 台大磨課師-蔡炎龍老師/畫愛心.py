# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:46:37 2019

@author: Home love
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,1000)
x = 16*(np.sin(t))**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
plt.xkcd()
plt.plot(x,y,'r')
plt.title('Ah Shan I Luv U',fontsize=24,color='r')