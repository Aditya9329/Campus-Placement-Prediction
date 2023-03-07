import cassandra
import pandas as pd 

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
  'secure_connect_bundle': 'secure-connect-cassandra-data.zip'
}
auth_provider = PlainTextAuthProvider('LDgoaZuXHUTZGgwgksUdzIwW', 'qOo7grC9O-h44fDDefnNakmLzan6bIGDnRG39LHOFQ3vJ2JDJ2JH+6FgjwCQ.Wxu.0aP4yMTozxRNUI_++mmTeopuK62lcQHs56wWswyAGZcR4s.EUtvzzCMZ5Lt0RXG')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

result = session.execute("select * from data_test.train")


row = result.one()
print(row)

"""
            letting the cassandra which
            key space we want to use.

"""

try:
    q = "use data_test"
    session.execute(q)
    print("use data_test")
except Exception as e:
    print("error:",e)

"""
            getting data from cassandra database 
            and converting it into the dataframe
            and storing the data as csv_file into the raw
            data_folder.
"""

df = pd.DataFrame(list(session.execute("select * from train")))
print(df.head())


df.to_csv('data_given/campusplacement.csv')

