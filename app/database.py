from sqlalchemy.orm import Session as SqlAlchSession
import sqlalchemy
import config.environment as env

connectionSetup = 'mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}'.format(
    username=env.DB_SQL_USERNAME,
    password=env.DB_SQL_PASSWORD,
    host=env.DB_SQL_HOST,
    port=env.DB_SQL_OUTPORT,
    dbname=env.DB_SQL_DBNAME,
)

engine = sqlalchemy.create_engine(
    connectionSetup, connect_args={'connect_timeout': 100000})


class Session(SqlAlchSession):
    def __init__(self):
        super().__init__(engine)


session = Session()
