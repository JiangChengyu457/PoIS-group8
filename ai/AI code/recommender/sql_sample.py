from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float

import pandas as pd

import config

user = config.DB_USER
password = config.PASSWORD
host = config.HOST
db_name = config.DATABASE

# engineの設定
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}')

# セッションの作成
db_session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
  )
)

# テーブルを作成する
Base = declarative_base()
Base.query  = db_session.query_property()

# DBにあるWineのデータを全件取得
db = db_session.query(Wine).all()
for row in db:
  # カラムを指定してデータを取得する
  print(row.alcohol)

