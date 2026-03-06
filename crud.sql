-- insert demo book
INSERT INTO book (title, author, publish_date, isbn)
VALUES ('Python Crash Course', 'Eric Matthes', '2016-11-01', '978-1593276034');

-- list all
SELECT * FROM book ORDER BY id;

-- search by exact title
SELECT * FROM book WHERE title = 'Python Crash Course' LIMIT 1;

-- delete by title
DELETE FROM book WHERE title = 'Python Crash Course';

-- update book info
UPDATE book
SET title = 'Fluent Python',
    author = 'Luciano Ramalho',
    publish_date = '2022-01-01',
    isbn = '978-1492056355'
WHERE title = 'Python Crash Course';
