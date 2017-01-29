from __future__ import division
import numpy as np
import scipy.spatial.distance as dist
from scipy import stats

# Load the data needed for Problems 1-3 

# Read the data
traindata_tmp = np.genfromtxt('train.csv', delimiter=',')
valdata_tmp = np.genfromtxt('val.csv', delimiter=',')

#The data which you will use to train LDA and kNN is called "trainingdata"
trainingdata = traindata_tmp[:,:2]
#The corresponding labels are in "traininglabels"
traininglabels = traindata_tmp[:,2]

#The data which you will use to validate LDA, kNN and the Bayes Classifier
#is called "valdata"
valdata = valdata_tmp[:,:2]
#The corresponding labels are in "vallabels"
vallabels = valdata_tmp[:,2]

# Some code to visualize decision regions in Problem 1 to 3; You don't need to look at this.
# adp = np.vstack([trainingdata,valdata])
# xmin,xmax = adp[:,0].min()-1, adp[:,0].max()+1
# ymin,ymax = adp[:,0].min()-1, adp[:,0].max()+1
# xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.05),np.arange(ymin, ymax, 0.05))
# drdata = np.c_[xx.ravel(), yy.ravel()]

def bayesClassifier(data,pi,means,cov):
    m_cov_prod =  np.dot(means, np.linalg.inv(cov))
    return np.log(pi) + np.dot(m_cov_prod,np.transpose(data)) - 1/2 * np.dot(m_cov_prod, means)

#The data which you will use to test the classifier is called "data"
data = np.copy(valdata)
#The labels are in "truelabels"
truelabels = np.copy(vallabels)

# scatter(data[:,0],data[:,1],c=truelabels)
# axis('tight')

cov   = np.array([[3,1],[1,3]])
pis   = np.array([1/3, 1/2, 1/6])
means = np.array([[5,5],[5,0], [-1,0]])

print bayesClassifier(data,pis[0], means[0], cov)

# pcolormesh(xx,yy,drB.reshape(xx.shape),alpha=0.1,antialiased=True)
# axis('tight')
# scatter(data[:,0],data[:,1],c=truelabels)
