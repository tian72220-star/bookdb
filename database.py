import sqlite3

DB_FILE = "library.db"

def get_conn():
    return sqlite3.connect(DB_FILE)

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                publish_date TEXT,
                isbn TEXT UNIQUE
            );
        """)
    print("数据库/表 已准备好 ✅")

# 追加的增删改查
def add_book(title, author, publish_date, isbn):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO book(title, author, publish_date, isbn) VALUES (?,?,?,?)",
            (title, author, publish_date, isbn)
        )

def find_book(title):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM book WHERE title = ? LIMIT 1", (title,))
        return cur.fetchone()

def list_books():
    with get_conn() as conn:
        return conn.execute("SELECT * FROM book ORDER BY id").fetchall()

def delete_book(title):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM book WHERE title = ?", (title,))
        return cur.rowcount

def update_book(old_title, new_title, new_author, new_date, new_isbn):
    with get_conn() as conn:
        cur = conn.execute(
            """UPDATE book
               SET title=?, author=?, publish_date=?, isbn=?
               WHERE title=?""",
            (new_title, new_author, new_date, new_isbn, old_title)
        )
        return cur.rowcount

if __name__ == "__main__":
    init_db()
