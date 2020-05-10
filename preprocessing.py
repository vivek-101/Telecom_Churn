import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler, OneHotEncoder, Normalizer, scale, MinMaxScaler

from load_data import telecom

#### Col Identifier ######
telecom['SeniorCitizen'] = telecom['SeniorCitizen'].map({1:'Yes',0:'No'})
telecom['TotalCharges'] = pd.to_numeric(telecom['TotalCharges'],errors='coerce')
ordinal_attr = ['PhoneService', 'PaperlessBilling', 'SeniorCitizen', 'Partner', 'Dependents']
dummy = ['Contract', 'PaymentMethod', 'gender', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
         'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
num_attr = ['tenure','MonthlyCharges','TotalCharges']
testing_churn = telecom[['Churn']]
testing_churn = testing_churn['Churn'].map({'Yes':1,'No':0})
telecom.drop('Churn',axis=1,inplace=True)
######## Pipeline ########
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('std_scale', MinMaxScaler(feature_range = (-1,1)))
])


full_pipeline = ColumnTransformer([
    ('num', num_pipeline,num_attr),
    ('ordinal', OrdinalEncoder(),ordinal_attr),
    ('cat', OneHotEncoder(drop='first',sparse=False),dummy)
])

# sample_telecom = telecom[0:3]
fitting = full_pipeline.fit(telecom)
cat_names = full_pipeline.named_transformers_.cat.get_feature_names(dummy)

def feature_ext(sample):
    int_cols = {
        'tenure':int,
        'MonthlyCharges':float,
        'TotalCharges':float
    }
    sample.columns = telecom.columns
    sample = sample.astype(int_cols)
    testing = fitting.transform(sample)
    testing = pd.DataFrame(testing,columns=list(num_attr)+ordinal_attr+list(cat_names))
    return testing


keep = ['tenure', 'MonthlyCharges', 'TotalCharges', 'PhoneService', 'PaperlessBilling', 'Contract_One year',
        'Contract_Two year', 'PaymentMethod_Electronic check', 'MultipleLines_No phone service',
        'InternetService_Fiber optic', 'OnlineSecurity_Yes', 'OnlineBackup_No internet service', 'TechSupport_Yes']
