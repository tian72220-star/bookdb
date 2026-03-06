CREATE TABLE IF NOT EXISTS book (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    title         TEXT NOT NULL,
    author        TEXT,
    publish_date  TEXT,
    isbn          TEXT UNIQUE
);