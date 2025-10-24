from flask import Flask, request, redirect, render_template, url_for
from database import (init_db, add_book, list_books, delete_book,
                      update_book, find_book)
import os

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    rows = list_books()
    return render_template('index.html', books=rows)

@app.route('/add', methods=['POST'])
def add():
    add_book(request.form['title'],
             request.form['author'],
             request.form['publish_date'],
             request.form['isbn'])
    return redirect(url_for('index'))

@app.route('/delete/<title>')
def delete(title):
    delete_book(title)
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword', '').strip()
    if not keyword:
        return redirect(url_for('index'))
    rows = [find_book(keyword)]
    rows = [r for r in rows if r]
    return render_template('index.html', books=rows, keyword=keyword)

@app.route('/edit', methods=['POST'])
def edit():
    update_book(request.form['old_title'],
                request.form['new_title'],
                request.form['new_author'],
                request.form['new_publish_date'],
                request.form['new_isbn'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
