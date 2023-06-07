import sqlite3

DB_FILE_NAME = 'example.db'

def init():
    with sqlite3.connect(DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM sqlite_schema WHERE type = 'table' AND name NOT LIKE 'sqlite_%'")
        if len(cur.fetchall()) == 0:
            # Create the db from scratch.
            print('Database schema not created yet. Creating...')
            cur.execute("create table items (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name text, done bool)")
            con.commit()
            print('Done!')


def get_list_items():
    with sqlite3.connect(DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM items")
        return cur.fetchall()


def create_list_item(name):
    with sqlite3.connect(DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO items (name, done) VALUES (?, ?)", (name, False))
        con.commit()


def toggle_list_item(id):
    with sqlite3.connect(DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute("UPDATE items SET done = ((done | 1) - (done & 1)) WHERE id = ?", (id,))
        con.commit()
