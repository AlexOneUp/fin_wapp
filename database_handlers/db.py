from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:SoyProducts17@localhost:3306/pytesting", echo=True)
conn = engine.connect()
result = engine.execute("select * from users")
aRet = result.fetchall()

