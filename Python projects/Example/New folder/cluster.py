from numpy import vstack,array
from numpy.random import rand

import matplotlib.pyplot as plt

from scipy.cluster.vq import kmeans,vq,whiten
data = vstack(((rand(20,2)+1),(rand(20,2)+3),(rand(20,2)+4.5)))
plt.plot(data[:,0],data[:,1],'go')

data = whiten(data)

centroids,distortion = kmeans(data,3)
 
print('centroids  : ',centroids)
print('distortion :',distortion)
plt.plot(data[:,0],data[:,1],'go',centroids[:,0],centroids[:,1],'bs')
plt.show() 
