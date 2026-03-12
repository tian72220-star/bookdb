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
    print("数据库/表 已准备好")

# ---------- 原有函数 ----------
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

# ---------- 新增：按 ID 操作（更稳）----------
def get_book_by_id(book_id):
    """用 ID 查单本书"""
    with get_conn() as conn:
        return conn.execute("SELECT * FROM book WHERE id = ?", (book_id,)).fetchone()

def delete_book_by_id(book_id):
    """用 ID 删除，返回 0 或 1（是否成功）"""
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM book WHERE id = ?", (book_id,))
        return cur.rowcount

def update_book_by_id(book_id, new_title, new_author, new_date, new_isbn):
    """用 ID 更新"""
    with get_conn() as conn:
        cur = conn.execute(
            """UPDATE book SET title=?, author=?, publish_date=?, isbn=? WHERE id=?""",
            (new_title, new_author, new_date, new_isbn, book_id)
        )
        return cur.rowcount