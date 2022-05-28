from dotenv import dotenv_values

env = dotenv_values(".env")

APP_PORT = env.get("APP_PORT")
APP_HOST = env.get("APP_HOST")
DB_SQL_HOST = env.get("DB_SQL_HOST")
DB_SQL_USERNAME = env.get("DB_SQL_USERNAME")
DB_SQL_PASSWORD = env.get("DB_SQL_PASSWORD")
DB_SQL_DBNAME = env.get("DB_SQL_DBNAME")
DB_SQL_INPORT = env.get("DB_SQL_INPORT")
DB_SQL_OUTPORT = env.get("DB_SQL_OUTPORT")
