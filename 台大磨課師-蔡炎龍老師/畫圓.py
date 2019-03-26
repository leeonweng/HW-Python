# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:22:44 2019

@author: Home love
"""

import matplotlib.pyplot as plt
import numpy as np
"""
x = np.linspace(5,-5,1000)
y = np.exp(x*2)
plt.plot(x,y)
"""
r = 2.0
a, b = (0, 0)

theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
fig = plt.figure() 
axes = fig.add_subplot(111) 
axes.plot(x, y)
axes.axis('equal')