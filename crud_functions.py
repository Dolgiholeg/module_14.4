import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL);  
''')

# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",(f"Product{i}", f"Описание{i}", f"{i*100}"))


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products_list = cursor.fetchall()
    return products_list



