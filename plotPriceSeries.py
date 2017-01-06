__author__ = 'seanhendryx'


import numpy as np
#import math
#from scipy.stats import skew, kurtosis, kurtosistest
import matplotlib.pyplot as plt
#from scipy.stats import norm, t
import pandas_datareader.data as web


# Fetching Yahoo! Finance for Apple stock data
data = web.DataReader("AAPL", data_source='yahoo',
                  start='2007-12-01', end='2016-2-20')['Adj Close']
cp = np.array(data.values)  # daily adj-close prices
ret = cp[1:]/cp[:-1] - 1    # compute daily returns

# Plotting Apple price- and return-series
plt.figure(num=2, figsize=(9, 6))
plt.subplot(2, 1, 1)
plt.plot(cp)
plt.axis("tight")
plt.ylabel("Apple Adj Close [USD]")
plt.subplot(2, 1, 2)
plt.plot(ret, color=(.6, .6, .6))
plt.axis("tight")
plt.ylabel("Daily Returns")
plt.xlabel("Days from 2007-12-01 to 2016-2-20")

plt.show()