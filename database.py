def init_db():
    with get_conn() as conn:
        # 书籍表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                publish_date TEXT,
                isbn TEXT UNIQUE
            );
        """)
        # 用户表（新增）
        conn.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0
            );
        """)
    print("数据库/表 已准备好")

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