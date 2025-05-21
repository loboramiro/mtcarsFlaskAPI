import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

mtcars = pd.read_csv("mtcars.csv")

predictors = [
    'cyl', 
    'disp',
    'hp',
    'drat',
    'wt',
    'qsec'
]

y = mtcars['mpg']
x = mtcars[predictors]

reg = LinearRegression().fit(x, y)

def predict(dict_values, predictors = predictors, reg = reg):
    x = np.array([float(dict_values[col]) for col in predictors])
    x = x.reshape(1,-1)
    y_pred = reg.predict(x)[0]

    return y_pred