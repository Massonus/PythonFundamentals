import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:root@localhost:5432/Test")
# engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:massonus@awseb-e-umvcxak4y3-stack-awsebrdsdatabase-9ldqegjv6dyg.cps2ceiewud2.eu-central-1.rds.amazonaws.com:5432/postgres")

# data = pd.read_sql('employee', engine)
#
# index = data[data['id'] == 1].index
#
# data.loc[index, 'name'] = 'Jordan'
# data.to_sql('employee', engine, if_exists='replace', index=False, index_label='id')
# # df1 = pd.DataFrame([{'name': 'asdfg'}])
# # df1.to_sql('employee', engine, if_exists='append', index=False, index_label='id')
# data = data.drop(index)
# data.to_sql('employee', engine, if_exists='replace', index=False, index_label='id')

# data = pd.read_sql('pending_users', engine)
# index = data[data['user_id'] == 661204444].index
# print(index)
# data = data.drop(index)
# data.to_sql('pending_users', engine, if_exists='replace', index=False, index_label='id')
