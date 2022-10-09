list_column = ['FirsName', 'LastName']

list_data = [('Jon', 'Yang'), ('Eugene', 'Huang'), ('Ruben', 'Torres'), ('Christy', 'Zhu'), 
('Elizabeth', 'Johnson'), ('Julio', 'Ruiz'), ('Janet', 'Alvarez'), ('Marco', 'Mehta'), ('Rob', 'Verhoff'), 
('Shannon', 'Carlson')]


for i in list_data:
    print(f"INSERT INTO customers ({list_column[0]}, {list_column[1]}) VALUES {i}")