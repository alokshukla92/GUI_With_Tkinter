import sqlite3

def connect():
    conn = sqlite3.connect("bookStore.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT,year INTEGER ,isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("bookStore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("bookStore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row



# If a user passes only one value e.g author, all other parameter will remain without a value and it will generate error
# So pass a empty string foreach of these parameters as defualt values


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("bookStore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("bookStore.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,)) # if there is only one parametr don't forget to add , after parameter
    conn.commit()
    conn.close()

def update(id, new_title, new_author, new_year, new_isbn):
    conn = sqlite3.connect("bookStore.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ?  WHERE id = ?",(new_title, new_author, new_year, new_isbn, id))
    conn.commit()
    conn.close()


connect()
# insert("The Dominator", "D.D Prince", 1995, 157946241)
# delete(2)
# update(1, 'The Earth', 'Alok Shuklaa', 2000, 8169573162)
# print(view())
# print(search(author="D.D Prince"))
