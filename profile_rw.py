import numpy as np
import matplotlib.pyplot as plt

data0 = np.loadtxt("traces_ID_0.dat", delimiter="," ,skiprows=1)
data1 = np.loadtxt("traces_ID_1.dat", delimiter="," ,skiprows=1)

data0r = np.delete(data0, np.where(data0[:,2]==1),0)
data0w = np.delete(data0, np.where(data0[:,2]==0),0)
data1r = np.delete(data1, np.where(data1[:,2]==1),0)
data1w = np.delete(data1, np.where(data1[:,2]==0),0)

fig = plt.figure()
ax0 = fig.add_subplot(223)

ax0.plot(data0w[:,1], data0w[:,7],'--o', color='red', label='AW Master 0. Num tests %d, B %d' %(len(data0w[:,1]), data0w[0,5]) )
ax0.plot(data1w[:,1], data1w[:,7],'--x', color='cyan', label='AW Master 1. Num tests %d, B %d' %(len(data1w[:,1]), data1w[0,5]) )

mean0w = np.mean(data0w[:,7])
mean1w = np.mean(data1w[:,7])

max_time = np.max([data0w[-1,1],data1w[-1,1]])

ax0.hlines(mean0w,0,max_time, color='red')
ax0.hlines(mean1w,0,max_time, color='cyan')

plt.ylabel('Util')
plt.xlabel('Time [ns]')
plt.legend()

ax2 = fig.add_subplot(221)

ax2.plot(data0w[:,0], data0w[:,4],'o', color='red', label='AW Master 0. Num tests %d, B %d' %(len(data0w[:,0]), data0w[0,5]) )
ax2.plot(data1w[:,0], data1w[:,4],'x', color='cyan', label='AW Master 1. Num tests %d, B %d' %(len(data1w[:,0]), data1w[0,5]) )
plt.ylabel('AW_valid latency')
plt.xlabel('Time [ns]')
plt.legend()

ax1 = fig.add_subplot(224)

ax1.plot(data0r[:,1], data0r[:,7],'--o', color='green', label='AR Master 0. Num tests %d, B %d' %(len(data0r[:,1]), data0r[0,5]) )
ax1.plot(data1r[:,1], data1r[:,7],'--x', color='blue', label='AR Master 1. Num tests %d, B %d' %(len(data1r[:,1]), data1r[0,5]) )

mean0r = np.mean(data0r[:,7])
mean1r = np.mean(data1r[:,7])

max_time = np.max([data0r[-1,1],data1r[-1,1]])
ax1.hlines(mean0r,0,max_time, color='blue')
ax1.hlines(mean1r,0,max_time, color='black')

plt.ylabel('Util')
plt.xlabel('Time [ns]')
plt.legend()

ax3 = fig.add_subplot(222)

ax3.plot(data0r[:,0], data0r[:,4],'o', color='green', label='AR Master 0. Num tests %d, B %d' %(len(data0w[:,0]), data0w[0,5]) )
ax3.plot(data1r[:,0], data1r[:,4],'x', color='blue', label='AR Master 1. Num tests %d, B %d' %(len(data1w[:,0]), data1w[0,5]) )
print(data0r[:,0])
print(data0r[:,4])
print(data1r[:,0])
print(data1r[:,4])

plt.ylabel('AR_ready latency')
plt.xlabel('Time [ns]')
plt.legend()

plt.show()
