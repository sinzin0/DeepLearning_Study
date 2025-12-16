# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:18:42 2024

@author: jyshin
"""

import numpy as np
import matplotlib.pyplot as plt

# sigmoid

# step
def step_function(x) :
    y = x > 0
    return y.astype(np.int32)

# RELU
def relu(x) :
    
    
    