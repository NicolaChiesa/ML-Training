# Making imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


plt.rcParams['figure.figsize'] = (10.0, 7.0)

# Preprocessing Input data
current_directory = os.getcwd()
dataFolder = os.path.join(current_directory,"Data")
file_path = os.path.join(dataFolder, "headBrain.csv")
data = pd.read_csv(file_path)

X = data.iloc[:, 2]
Y = data.iloc[:, 3]
# plt.scatter(X, Y)
# plt.xlabel('Age')
# plt.ylabel('Head Circonference')
# plt.show()

# Building the model
X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean

print (m, c)

# Making predictions
Y_pred = m*X + c


plt.scatter(X, Y) # actual
plt.xlabel('Head Size(cm^3)')
plt.ylabel('Brain Weight(grams)')
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()
