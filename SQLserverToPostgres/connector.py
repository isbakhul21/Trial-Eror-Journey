#import needed libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
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
src_cursor.execute(""" SELECT TOP 10 FirstName, LastName 
FROM AdventureWorksDW2019.dbo.DimCustomer;""")
src_tables = src_cursor.fetchall()

print(src_tables)