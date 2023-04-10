import sqlite3


connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("create table gta(release_year integer,release_name text,city text)")
cursor.execute("create table pani_puri123 (id integer,name text,quantity integer,unit text)")

release_list =[(1997,"gta","gruensey"),
              (1999,"gta 2","All of usa"),
              (2001,"gta 3","liberty")
]
pani_puri123 = [(0, "white_peas", 500, "gram"),
                (1, "puri", 1, "packet"),
                (2, "potato", 500, "gram"),
                (3, "tamarind_water", 1, "litre"),
                (4, "coriander_water", 1, "litre")
                ]

cursor.executemany("insert into gta values (?,?,?)",release_list)
cursor.executemany("insert into pani_puri123 values (?,?,?,?)", pani_puri123)

# print database row
for row in cursor.execute("select * from gta"):
    print(row)
for row in cursor.execute("select * from pani_puri123"):
    print(row)

cursor.execute("select * from gta where city=:c",{"c":"liberty"})
gta_s = cursor.fetchall()

connection.close()