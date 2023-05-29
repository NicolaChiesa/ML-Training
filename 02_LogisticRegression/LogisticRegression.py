#import libraries and files
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 

# load tic-tac-toe data
data = pd.read_csv("tic-tac-toe.data", sep=",")
data.rename(columns={'x': 'top left', 'x.1': 'top middle', 'x.2': 'top right','x.3': 'middle left', 'o': 'middle middle', 'o.1' : 'middle right', 'x.4' : 'bottom left', 'o.2' : 'bottom middle', 'o.3':'bottom right','positive' : 'outcome'},inplace=True)
data.head(3)