#!/usr/bin/python

import pandas as pd
import numpy as np
import joblib
import sys
import os

def pred_car_price(year, mileage, state, make, model):

    # Features
    car_info = [(year, mileage, state, make, model)]
    car_info = pd.DataFrame(car_info, columns=['Year', 'Mileage', 'State', 'Make', 'Model'])#.to_numpy()
    
    # Model train
    regressor = joblib.load(os.path.dirname(__file__) + '/car_price.pkl') 

    # Make prediction
    p1 = regressor.predict(car_info)

    return p1

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please insert a car info')
    else:
        car_info = sys.argv[1]
        p1 = pred_car_price(car_info)
        print(car_info)
        print('Car Price: ', p1)