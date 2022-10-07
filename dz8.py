import sqlite3
from sqlite3 import Error
from termcolor import cprint

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)

    return conn

def create_table(conn, sql):
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            # conn.commit()
        except Error:
            print(Error)


def create_product(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)

def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        cprint("LIST OF ALL PRODUCTS: ", color="green")
        for row in rows:
            cprint(row, color="blue")
    except Error:

        print(Error)

connection = create_connection("hw.db")


create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''
if connection is not None:
    cprint("Connection!", color="red")
    create_table(connection, create_products_table)

    # delete_product(connection, (2))

    # select_all_products(connection)

    # update_product_quantity(connection, (999994.99, 2))

    # create_product(connection, ("Chocolate", 74.99, 2000))
    # create_product(connection, ("Oil", 137.45, 400))
    # create_product(connection, ("Bread", 35.56, 500))
    # create_product(connection, ("Banana", 120.00, 4600))
    # create_product(connection, ("Tomato", 65.89, 20005))
    # create_product(connection, ("Sugar", 90.00, 46500))
    # create_product(connection, ("Sausage", 378.87, 5600))
    # create_product(connection, ("Avocado", 94.68, 5400))
    # create_product(connection, ("Apple", 59.77, 540))
    # create_product(connection, ("Melon", 200.00, 450))
    # create_product(connection, ("Cheese", 457.56, 4500))
    # create_product(connection, ("Egg", 98.65, 65760))
    # create_product(connection, ("Milk", 85.33, 4740))
    # create_product(connection, ("Cracker", 45.00, 4700))
    # create_product(connection, ("Juice", 86.34, 24760))

    cprint("Done", color="red")
