import sqlite3

DB_FILE = "library.db"

def get_conn():
    return sqlite3.connect(DB_FILE, check_same_thread=False)

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
        conn.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0
            );
        """)
    print("数据库/表 已准备好")

def add_book(title, author, publish_date, isbn):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO book(title, author, publish_date, isbn) VALUES (?,?,?,?)",
            (title, author, publish_date, isbn)
        )

def list_books():
    with get_conn() as conn:
        return conn.execute("SELECT * FROM book ORDER BY id").fetchall()

def search_books(keyword):
    with get_conn() as conn:
        cur = conn.execute(
            "SELECT * FROM book WHERE title LIKE ? ORDER BY id",
            (f"%{keyword}%",)
        )
        return cur.fetchall()

def get_book_by_id(book_id):
    with get_conn() as conn:
        return conn.execute("SELECT * FROM book WHERE id = ?", (book_id,)).fetchone()

def delete_book_by_id(book_id):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM book WHERE id = ?", (book_id,))
        return cur.rowcount

def update_book_by_id(book_id, new_title, new_author, new_date, new_isbn):
    with get_conn() as conn:
        cur = conn.execute(
            """UPDATE book SET title=?, author=?, publish_date=?, isbn=? WHERE id=?""",
            (new_title, new_author, new_date, new_isbn, book_id)
        )
        return cur.rowcount

def get_stats():
    with get_conn() as conn:
        total = conn.execute("SELECT COUNT(*) FROM book").fetchone()[0]
        latest = conn.execute("SELECT title FROM book ORDER BY id DESC LIMIT 1").fetchone()
        return total, latest[0] if latest else "No books yet"

def add_user(username, password, is_admin=0):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO user(username, password, is_admin) VALUES (?,?,?)",
            (username, password, is_admin)
        )

def find_user(username):
    with get_conn() as conn:
        return conn.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

def check_user(username, password):
    with get_conn() as conn:
        return conn.execute(
            "SELECT * FROM user WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
