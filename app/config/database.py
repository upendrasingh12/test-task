# config/database.py
import pymysql.cursors
from app.config.settings import settings

def connect_to_database():
    print("hi")
    try:
        connection_online = connect_database()
        print("connection_online", connection_online)
        return connection_online
    except:
        pass

    try:
        connection_offline = connect_database_local()
        return connection_offline
    except:
        pass

    raise Exception("Could not connect to the database")

def connect_database():
    connection = pymysql.connect(
        host=settings.db_host,
        user=settings.db_user,
        password=settings.db_password,
        db=settings.db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def connect_database_local():
    connection = pymysql.connect(
        host=settings.db_host_local,
        user=settings.db_user_local,
        password=settings.db_password_local,
        db=settings.db_name_local,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# mydb_local = mysql.connector.connect(
#   host=settings.db_host_local,
#   user=settings.db_user_local,
#   password=settings.db_password_local,
#   database=settings.db_name_local
# )