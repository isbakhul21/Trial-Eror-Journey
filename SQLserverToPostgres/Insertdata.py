
import psycopg2


list_column = ['FirstName', 'LastName']
ourlist = [('Jon', 'Yang'), ('Eugene', 'Huang'), ('Ruben', 'Torres'), ('Christy', 'Zhu'), 
('Elizabeth', 'Johnson'), ('Julio', 'Ruiz'), ('Janet', 'Alvarez'), ('Marco', 'Mehta'), ('Rob', 'Verhoff'), 
('Shannon', 'Carlson')]

sql = "INSERT INTO customers (FirstName, LastName) VALUES (%s, %s)"

con = psycopg2.connect(
            host="localhost",
            user="etl", 
            password="demopass",
            database="DWH",
            port=5432)

cur = con.cursor()
cur.execute(f"CREATE TABLE Customers ({list_column[0]} character(50), {list_column[1]} character(50))")
cur.executemany(sql, ourlist)
con.commit()

cur.close()
con.close()