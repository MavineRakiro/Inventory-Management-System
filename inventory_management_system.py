from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
import xgboost

#we are loading the model using pickle
model = pickle.load(open('inventory_management_system', 'rb'))

def predict_inventory(df):
    predictions=model.predict(df)
    df['predictions']=predictions
    return(df)