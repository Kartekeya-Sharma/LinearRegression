# -*- coding: utf-8 -*-
"""LinearRegression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xpEyNBDjrqQGgthfAkuOM3izOfSr4W-r
"""


import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
weight=[  16, 25 , 36, 49, 64, 81, 100]
reg=linear_model.LinearRegression()
reg.fit(height,weight)
X_height=[[12.0]]
print(reg.predict(X_height))

