{\rtf1\ansi\ansicpg936\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import sqlite3\
\
DB_FILE = "library.db"\
\
def get_conn():\
    return sqlite3.connect(DB_FILE, check_same_thread=False)\
\
def init_db():\
    with get_conn() as conn:\
        conn.execute("""\
            CREATE TABLE IF NOT EXISTS book (\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                title TEXT NOT NULL,\
                author TEXT,\
                publish_date TEXT,\
                isbn TEXT UNIQUE\
            );\
        """)\
    print("\uc0\u25968 \u25454 \u24211 /\u34920  \u24050 \u20934 \u22791 \u22909 ")\
\
# ---------- \uc0\u21407 \u26377 \u20989 \u25968  ----------\
def add_book(title, author, publish_date, isbn):\
    with get_conn() as conn:\
        conn.execute(\
            "INSERT INTO book(title, author, publish_date, isbn) VALUES (?,?,?,?)",\
            (title, author, publish_date, isbn)\
        )\
\
def list_books():\
    with get_conn() as conn:\
        return conn.execute("SELECT * FROM book ORDER BY id").fetchall()\
\
def find_book(title):\
    with get_conn() as conn:\
        return conn.execute("SELECT * FROM book WHERE title = ? LIMIT 1", (title,)).fetchone()\
\
def delete_book(title):\
    with get_conn() as conn:\
        cur = conn.execute("DELETE FROM book WHERE title = ?", (title,))\
        return cur.rowcount\
\
def update_book(old_title, new_title, new_author, new_date, new_isbn):\
    with get_conn() as conn:\
        cur = conn.execute(\
            """UPDATE book SET title=?, author=?, publish_date=?, isbn=? WHERE title=?""",\
            (new_title, new_author, new_date, new_isbn, old_title)\
        )\
        return cur.rowcount\
\
# ---------- \uc0\u26032 \u22686 \u65306 \u27169 \u31946 \u25628 \u32034  ----------\
def search_books(keyword):\
    """\uc0\u25353 \u20851 \u38190 \u35789 \u27169 \u31946 \u25628 \u32034 \u20070 \u21517 """\
    with get_conn() as conn:\
        cur = conn.execute(\
            "SELECT * FROM book WHERE title LIKE ? ORDER BY id",\
            (f"%\{keyword\}%",)\
        )\
        return cur.fetchall()}