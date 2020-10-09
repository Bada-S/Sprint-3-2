import sqlite3

conn = sqlite3.connect(r'C:\Users\james\Downloads\northwind_small(1).sqlite3')
curs = conn.cursor()

print(curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall())

curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()

query = """
    SELECT DISTINCT OrderDetail.ProductId, OrderDetail.UnitPrice, ProductDetails_V.ProductName
    FROM OrderDetail
    INNER JOIN ProductDetails_V on OrderDetail.ProductId=ProductDetails_V.Id
    ORDER BY OrderDetail.UnitPrice DESC
    LIMIT 10
"""

print(curs.execute(query).fetchall())
