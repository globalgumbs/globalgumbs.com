import pickle
import numpy as np

model_path = "./model1.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

X_test = np.array([ 3.4       , -5.43157895, -2.98947368,  2.18684211,  5.20789474,
        0.21578947,  1.70789474, -3.08684211, -6.47631579,  1.30789474,
        2.54736842, -1.89736842,  3.42368421,  0.024     ]).reshape(1,-1)
print(X_test)
y = model.predict(X_test)
print(int(y[0]))