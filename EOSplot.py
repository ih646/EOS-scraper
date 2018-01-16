from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


price,vol,marketprice,time=np.loadtxt("EOS_realtime.csv",delimiter=',',skiprows=1,unpack=True)

print price,vol,marketprice,time


plt.figure(1)
plt.plot(time,price)
plt.ylim(min(price),max(price))
plt.axhline(color="gray", zorder=-1)
plt.xlabel("time(s)")
plt.ylabel("price(ETH)")

plt.figure(2)
plt.plot(time,vol)
plt.ylim(min(vol),max(vol))
plt.axhline(color="gray", zorder=-1)
plt.xlabel("time(s)")
plt.ylabel("vol(ETH)")

plt.figure(3)
plt.plot(time,marketprice)
plt.ylim(min(marketprice)-0.10*min(marketprice),max(marketprice)+0.10*max(marketprice))
plt.axhline(color="gray", zorder=-1)
plt.xlabel("time(s)")
plt.ylabel("marketprice(ETH)")


plt.show()