import pandas as pd
import ibm_db,ibm_db_dbi

dsn_hostname = "dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net"  # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "bfx87377"  # e.g. "abc12345"
dsn_pwd = "bct9s3cq6r@ln7zv"  # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"  # e.g. "BLUDB"
dsn_port = "50000"  # e.g. "50000"
dsn_protocol = "TCPIP"  # i.e. "TCPIP"

# Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print("Unable to connect: ", ibm_db.conn_errormsg())
# temp =
sql_int = "SELECT * FROM INT_DATA"
sql_cust = "SELECT * FROM CUST_DATA"
sql_churn = "SELECT * FROM CHURN_DATA"
# stmt = ibm_db.exec_immediate(conn, sql)
# int_data = pd.DataFrame()
conn_handle = ibm_db_dbi.Connection(conn)
internet_data = pd.read_sql(sql_int, conn_handle)
customer_data = pd.read_sql(sql_cust, conn_handle)
churn_data = pd.read_sql(sql_churn, conn_handle)

####Merging Data #######
df_1 = pd.merge(churn_data, customer_data, how='inner', on='customerID')
telecom = pd.merge(df_1, internet_data, how='inner', on='customerID')
