import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:root@localhost:5432/Test")
# engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:massonus@awseb-e-umvcxak4y3-stack-awsebrdsdatabase-9ldqegjv6dyg.cps2ceiewud2.eu-central-1.rds.amazonaws.com:5432/postgres")

print(pd.read_sql('employee', engine))

df1 = pd.DataFrame([{'name': 'asdfg'}])
df1.to_sql('employee', engine, if_exists='append', index=False, index_label='id')
