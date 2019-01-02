from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:pw@localhost:port#/pytesting", echo=True)
conn = engine.connect()
result = engine.execute("select * from users")
aRet = result.fetchall()

