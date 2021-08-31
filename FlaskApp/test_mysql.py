import mysql.connector as sql
import pandas as pd


connection = sql.connect(
    host = '192.168.100.5',
    user = 'shantam',
    password = '123',
    port = '3306',
    auth_plugin = 'mysql_native_password',
    database = 'DEMO_DB'
)
query = 'SELECT * from EMPLOYEES'

with connection.cursor() as cursor:
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        print(row)


# sqlengine = create_engine('mysql+pymysql://shantam:123:@192.168.100.5/DEMO_DB', pool_recycle = 3600)
# dbConn = sqlengine.connect()
# data = pd.read_csv('/home/vm1/Desktop/employees.csv')

# try:
#     frame = data.to_sql('employees', dbConn, if_exists = 'fail')
# except Exception as ex:
#     print(ex)
# else:
#     print("table created")
