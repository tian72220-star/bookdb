from flask import Flask, request, redirect, render_template, url_for
from database import (init_db, add_book, list_books, delete_book,
                      update_book, find_book)

app = Flask(__name__)
init_db()

# ---------- 已有路由 ----------
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

# ---------- 新增路由 ----------
@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword', '').strip()
    if not keyword:
        return redirect(url_for('index'))
    rows = [find_book(keyword)]          # 精确匹配（后面可改模糊）
    rows = [r for r in rows if r]        # 去掉 None
    return render_template('index.html', books=rows, keyword=keyword)

@app.route('/edit', methods=['POST'])
def edit():
    update_book(request.form['old_title'],
                request.form['new_title'],
                request.form['new_author'],
                request.form['new_publish_date'],
                request.form['new_isbn'])
    return redirect(url_for('index'))
from flask import Flask, request, redirect, render_template
from database import init_db, add_book, list_books, delete_book, update_book

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
    return redirect('/')

@app.route('/delete/<title>')
def delete(title):
    delete_book(title)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    update_book(request.form['old_title'],
                request.form['new_title'],
                request.form['new_author'],
                request.form['new_publish_date'],
                request.form['new_isbn'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
