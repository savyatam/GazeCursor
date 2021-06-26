import numpy as np 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score
from sklearn.multioutput import MultiOutputRegressor
import matplotlib.pyplot as plt
from math import sqrt
import pickle
import os


df = pd.read_csv('data.csv')
y = df['CursorX']
y2 = df['CursorY']
y_y = pd.concat([y,y2],axis=1)
X = df.drop(['CursorX','CursorY'],axis=1)


X_train_all, X_test_all, yy_train, yy_test = train_test_split(X, y_y, test_size=0.05)
RF_multi = RandomForestRegressor(n_estimators=100, random_state=42)
RF_multi.fit(X_train_all, yy_train)
print(mean_squared_error(yy_test, RF_multi.predict(X_test_all)))

preds = np.stack([t.predict(X_test_all) for t in RF_multi.estimators_])
preds[:,0], np.mean(preds[:,0]), yy_test
plt.plot([r2_score(yy_test, np.mean(preds[:i+1], axis=0)) for i in range(100)]);

myself = [251 ,239,	327 ,	244 ,	30.594117 ,	10.049876 ,	33.241540 ,	11.180340]
myself = np.array(myself)
myself = np.reshape(myself, (1,8))
myselfDF = pd.DataFrame(myself)
myselfDF.columns = ['LeftY', 	'RightY' ,	'LeftW' ,	'LeftH' ,	'RighttW', 	'RightH', 	'CursorX' ,	'CursorY']
myselfDF

print(RF_multi.predict(myselfDF))

# save the model to disk
filename = 'model.sav'
pickle.dump(RF_multi, open(filename, 'wb'))
 
