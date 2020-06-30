import pickle
from sklearn.linear_model import LogisticRegression
from preprocessing import keep,feature_ext
from load_data import telecom

testing = feature_ext(telecom)
testing_churn = testing[['Churn']]
testing_data = testing
testing_data.drop('Churn',axis = 1, inplace=True)

log = LogisticRegression()
log.fit(testing_data[keep], testing_churn.values.ravel())
pickle.dump(log, open("churn_model.pkl", "wb"))
# print(testing_churn.values.ravel().shape,testing_data.shape)
# log.predict(testing_data.iloc[0])