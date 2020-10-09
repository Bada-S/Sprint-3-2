import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

table = """
    Create Table IF NOT EXISTS demo (
        a text NOT NULL,
        x integer,
        y integer
    );
"""

insert = """
    INSERT INTO demo (a, x, y)
    VALUES ('g', 3, 9) 
"""
insert2 = """
    INSERT INTO demo (a, x, y)
    VALUES ('v', 5, 7)
    """
insert3 = """
    INSERT INTO demo (a, x, y)
    VALUES ('f', 8, 7)
"""

curs.execute(table)
curs.execute(insert)
curs.execute(insert2)
curs.execute(insert3)

query = """
    SELECT count(a)
    FROM demo
"""
print(curs.execute(query).fetchall())

query2 = """
    SELECT count(x) + count(y)
    FROM demo
    WHERE x>5 and y>5
"""
print(curs.execute(query2).fetchall())

query3 = """
    SELECT count(DISTINCT y)
    FROM demo
"""
print(curs.execute(query3).fetchall())