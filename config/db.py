from sqlalchemy import create_engine, MetaData

user = 'root'
passUser = 'S3cret'
host = 'localhost'
port = '3306'
db = 'fast_api'

engine = create_engine(f"mysql+pymysql://{user}:{passUser}@{host}:{port}/{db}")
meta = MetaData()

conn = engine.connect()