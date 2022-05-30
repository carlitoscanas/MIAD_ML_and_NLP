#!/usr/bin/python

import pandas as pd
import numpy as np
import joblib
import sys
import os
from sklearn.feature_extraction.text import CountVectorizer

def pred_movie_genre (plot):

    # Features
    vect = joblib.load(os.path.dirname(__file__) + '/vect.pkl') 
    X_test_dtm = vect.transform(pd.Series(plot))

    # Model train
    clf = joblib.load(os.path.dirname(__file__) + '/movie_genre.pkl') 

    # Make prediction
    p1 = clf.predict_proba(X_test_dtm)

    cols = ['p_Action', 'p_Adventure', 'p_Animation', 'p_Biography', 'p_Comedy', 'p_Crime', 'p_Documentary', 'p_Drama', 'p_Family',
            'p_Fantasy', 'p_Film-Noir', 'p_History', 'p_Horror', 'p_Music', 'p_Musical', 'p_Mystery', 'p_News', 'p_Romance',
            'p_Sci-Fi', 'p_Short', 'p_Sport', 'p_Thriller', 'p_War', 'p_Western']
    strng = ''

    for i in range(len(cols)):
        strng += cols[i] + ': ' + str(p1[0,i]) + ' '

    return strng

'''
if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print('Please insert a car info')
    else:
        car_info = sys.argv[1]
        p1 = pred_car_price(car_info)
        print(car_info)
        print('Car Price: ', p1)
'''