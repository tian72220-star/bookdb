import os
from flask import Flask, request, redirect, render_template, url_for
from database import (init_db, add_book, list_books, delete_book_by_id,
                      update_book_by_id, search_books, get_book_by_id, get_stats)

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

init_db()

@app.route('/')
def index():
    keyword = request.args.get('keyword', '').strip()
    rows = search_books(keyword) if keyword else list_books()
    total, latest = get_stats()  # 获取统计信息
    return render_template('index.html', books=rows, keyword=keyword, total=total, latest=latest)

@app.route('/add', methods=['POST'])
def add():
    add_book(request.form['title'],
             request.form['author'],
             request.form['publish_date'],
             request.form['isbn'])
    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>')
def delete(book_id):
    delete_book_by_id(book_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:book_id>')
def edit_page(book_id):
    book = get_book_by_id(book_id)
    return render_template('edit.html', book=book)

@app.route('/update/<int:book_id>', methods=['POST'])
def update(book_id):
    update_book_by_id(book_id,
                      request.form['title'],
                      request.form['author'],
                      request.form['publish_date'],
                      request.form['isbn'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))