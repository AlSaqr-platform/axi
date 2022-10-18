import numpy as np
import matplotlib.pyplot as plt

data0 = np.loadtxt("traces_ID_0.dat", delimiter="," ,skiprows=1)
data1 = np.loadtxt("traces_ID_1.dat", delimiter="," ,skiprows=1)

data0r = np.delete(data0, np.where(data0[:,1]==0),0)
data0w = np.delete(data0, np.where(data0[:,1]==1),0)
data1r = np.delete(data1, np.where(data1[:,1]==0),0)
data1w = np.delete(data1, np.where(data1[:,1]==1),0)

fig = plt.figure()
ax0 = fig.add_subplot(111)

ax0.plot(data0w[:,0], data0w[:,6],'--o', color='red', label='AW Master 0. Num tests %d, B %d' %(len(data0w[:,0]), data0w[0,4]) )
ax0.plot(data1w[:,0], data1w[:,6],'--x', color='cyan', label='AW Master 1. Num tests %d, B %d' %(len(data1w[:,0]), data1w[0,4]) )

mean0 = np.mean(data0w[:,6])
mean1 = np.mean(data1w[:,6])

ax0.plot(data0r[:,0], data0r[:,6],'--o', color='blue', label='AR Master 0. Num tests %d, B %d' %(len(data0r[:,0]), data0r[0,4]) )
ax0.plot(data1r[:,0], data1r[:,6],'--x', color='black', label='AR Master 1. Num tests %d, B %d' %(len(data1r[:,0]), data1r[0,4]) )

mean0w = np.mean(data0w[:,6])
mean1w = np.mean(data1w[:,6])
mean0r = np.mean(data0r[:,6])
mean1r = np.mean(data1r[:,6])

max_time = np.max([data0w[-1,0],data1w[-1,0],data0r[-1,0],data1r[-1,0]])

ax0.hlines(mean0w,0,max_time, color='red')
ax0.hlines(mean1w,0,max_time, color='cyan')
ax0.hlines(mean0r,0,max_time, color='blue')
ax0.hlines(mean1r,0,max_time, color='black')

plt.ylabel('Util')
plt.xlabel('Time [ns]')
plt.legend()
plt.show()
