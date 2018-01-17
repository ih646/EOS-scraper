from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#unpacking the collected data into the appropriate arrays
price,vol,marketprice,time=np.loadtxt("EOS_realtime.csv",delimiter=',',skiprows=1,unpack=True)

#plot of price vs time
plt.figure(1)
plt.plot(time,price)
plt.ylim(min(price),max(price))
plt.axhline(color="gray", zorder=-1)
plt.xlabel("time(s)")
plt.ylabel("price(ETH)")

#plot of volume vs time
plt.figure(2)
plt.plot(time,vol)
plt.ylim(min(vol),max(vol))
plt.axhline(color="gray", zorder=-1)
plt.xlabel("time(s)")
plt.ylabel("vol(ETH)")

#plot of market price vs time. Note: this plot will be a straight line unless scraper is running for a long time
#as market price fluctuation is a lot slower
plt.figure(3)
plt.plot(time,marketprice)
plt.ylim(min(marketprice)-0.10*min(marketprice),max(marketprice)+0.10*max(marketprice))
plt.axhline(color="gray", zorder=-1)
plt.xlabel("time(s)")
plt.ylabel("marketprice(ETH)")


plt.show()