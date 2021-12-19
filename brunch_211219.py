import numpy as np
import matplotlib.pylab as plt

def function(x):
    return pow(x,3)

x = np.arange(-5, 5, 0.1)
y = function(x) #<class 'numpy.float64'>
plt.plot(x, y)
plt.xlim(-6,6)  #x좌표 범위 설정
plt.ylim(-130, 130) #y좌표 범위 설정
plt.show()