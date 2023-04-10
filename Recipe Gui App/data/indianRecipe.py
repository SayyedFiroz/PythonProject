import sqlite3

connection = sqlite3.connect("indianRecipes.db")
cursor = connection.cursor()

cursor.execute("create table panipuri (id integer,name text,quantity integer,unit text)")
cursor.execute("create table bhelpuri (id integer,name text,quantity integer,unit text)")
cursor.execute("create table whitepeaspuri (id integer,name text,quantity integer,unit text)")

ingredient = [(0, 'white_peas', 500, 'gram'),
                (1, 'puri', 1, 'packet'),
                (2, 'potato', 500, 'gram'),
                (3, 'tamarind_water', 1, 'litre'),
                ]
ingredients = [(0, 'puffed_rice', 500, 'gram'),
                 (1, 'tomato', 200, 'gram'),
                 (2, 'potato', 200, 'gram'),
                 (3, 'onion', 100, 'gram'),


                 ]

ingredientss = [(0, 'white_peas', 500, 'gram'),
                      (1, 'puri', 1, 'packet'),
                      (2, 'potato', 500, 'gram'),
                      (3, 'tamarind_water', 1, 'litre')
                      ]

cursor.executemany("insert into panipuri values (?,?,?,?)", ingredient)
cursor.executemany("insert into bhelpuri values (?,?,?,?)", ingredients)
cursor.executemany("insert into whitepeaspuri values (?,?,?,?)", ingredientss)


for i in cursor.execute('select * from panipuri'):
    print(i)

for i in cursor.execute('select * from bhelpuri'):
    print(i)
for i in cursor.execute('select * from whitepeaspuri'):
    print(i)

cursor.fetchall()

connection.close()
