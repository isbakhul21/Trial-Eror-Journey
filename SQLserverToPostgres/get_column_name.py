#import needed libraries
from sqlalchemy import create_engine
import pyodbc
import os


#get password from environmnet var
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
#sql db details
driver = "{SQL Server Native Client 11.0}"
server = "LAPTOP-RR6QESQB"
database = "AdventureWorksDW2019;"

src_conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + '\SQLEXPRESS' + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
src_cursor = src_conn.cursor()

# execute query
sql =   """
        SELECT c.COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS c
        WHERE TABLE_NAME = 'DimCustomer' 
        AND COLUMN_NAME IN ('FirstName', 'LastName');
        """

sqls_get_data = """
                SELECT TOP 10 FirstName, LastName 
                FROM AdventureWorksDW2019.dbo.DimCustomer;
                """
src_cursor.execute(sql)
src_Column_name = src_cursor.fetchall()
#Merubah Data Loop ke Data List
column_name = [c[0] for c in src_Column_name]

src_cursor.execute(sqls_get_data)
src_column_data = src_cursor.fetchall()

column_data = [d[0] for d in src_column_data]


print(column_name)
print(src_column_data)