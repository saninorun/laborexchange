from databases import Database
from sqlalchemy import create_engine, MetaData
#from core.config import DATABASE_URL

database = Database("postgresql://root:root@localhost:32700/employment_exchange")
metadata = MetaData()
engine = create_engine("postgresql://root:root@localhost:32700/employment_exchange")
