
# # Description:                                                                                                                   
# The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset.

# Attributes:
# 1. Glucose Level
# 2. BMI
# 3. Blood pressure
# 4. Pregnancies
# 5. Skin thickness
# 6. Insulin
# 7. Diabetes pedigree function
# 8. Age
# 9. Outcome

# # Step 0: Import libraries and Dataset

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pickle

print('import successfull')

FILE = 'diabetes.csv'
df = pd.read_csv(f'./src/{FILE}')

#print(df.head())

#defining dependent and independent variable 
X = df.iloc[:,[0,1,2,3,4, 5, 7]].values
y = df.iloc[:,8].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print(cm)


MODEL= 'my_model.pkl'
SCALAR = 'transformer.pkl'
pickle.dump(sc, open(f'./models/{SCALAR}','wb'))
pickle.dump(classifier, open(f'./models/{MODEL}','wb'))









