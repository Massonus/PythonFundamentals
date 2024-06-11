import sqlalchemy
import pandas as pd
import numpy
import base64
import bcrypt
from passlib.hash import bcrypt

# engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:root@localhost:5432/Test")
# engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:massonus@awseb-e-umvcxak4y3-stack-awsebrdsdatabase-9ldqegjv6dyg.cps2ceiewud2.eu-central-1.rds.amazonaws.com:5432/postgres")
#
# data = pd.read_sql('product', engine)

# bot.send_message(message.chat.id, message.chat.id)
# bot.send_message(message.from_user.id, message.chat.id)
#
# index = data[data['id'] == 1].index
#
# data.loc[index, 'name'] = 'Jordan'
# data.to_sql('employee', engine, if_exists='replace', index=False, index_label='id')
# df1 = pd.DataFrame([{'name': 'asdfg'}])
# df1.to_sql('employee', engine, if_exists='append', index=False, index_label='id')
# data = data.drop(index)
# data.to_sql('employee', engine, if_exists='replace', index=False, index_label='id')

# data = pd.read_sql('pending_users', engine)
# index = data[data['user_id'] == 661204444].index
# print(index)
# data = data.drop(index)
# data.to_sql('pending_users', engine, if_exists='replace', index=False, index_label='id')

# print(bcrypt.verify("2fQC6JZhEx6vwYLHomXu", "$2a$10$wwxZEFYBZMdv7A4544B6c.8L5FG6.8ejStgnLeCNrmBoipy5idK7K"))
# print(bcrypt.hash('pass'))

# try:
#     user_id = data['telegram_id'].values.tolist()
# except KeyError:
#     data['telegram_id'] = [0] * len(data)
#     data.to_sql('consumer', engine, if_exists='replace', index=False, index_label='id')


# df1 = pd.DataFrame([{'username': 'asdfg'}])
# df1.to_sql('consumer', engine, if_exists='append', index=False, index_label='id')
# lista = data['id'].values.tolist()
# print(lista, max(lista))

# basket_object_data = pd.read_sql('basket_object', engine)
# basket_object_data.loc[basket_object_data['id'] == 63, 'amount'] += 1
# basket_object_data.to_sql('basket_object', engine, if_exists='replace', index=False, index_label='id')
