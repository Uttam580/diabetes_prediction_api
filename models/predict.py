MODEL= 'my_model.pkl'
SCALAR= 'transformer.pkl'

import pickle
import numpy as np

model = pickle.load(open(f'./models/{MODEL}','rb'))
sc = pickle.load(open(f'./models/{SCALAR}','rb'))
print(model.predict(sc.transform(np.array([[1,93,70,31,0,30.4,23]]))))