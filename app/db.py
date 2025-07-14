import sqlite3

def connect_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        code TEXT,
                        image_path TEXT
                    )''')
    conn.commit()
    return conn

def get_products_without_images():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, code FROM products WHERE image_path IS NULL")
    return cursor.fetchall()

def update_image_path(product_id, path):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET image_path = ? WHERE id = ?", (path, product_id))
    conn.commit()
    conn.close()
