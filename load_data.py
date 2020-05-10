import pandas as pd

### Loading Data #######
churn_data = pd.read_csv(r'C:\Users\ASUS\Desktop\DS\LogisticReg\churn_data.csv')
customer_data = pd.read_csv(r'C:\Users\ASUS\Desktop\DS\LogisticReg\customer_data.csv')
internet_data = pd.read_csv(r'C:\Users\ASUS\Desktop\DS\LogisticReg\internet_data.csv')

### Merging Data #######
df_1 = pd.merge(churn_data, customer_data, how='inner', on='customerID')
telecom = pd.merge(df_1, internet_data, how='inner', on='customerID')
