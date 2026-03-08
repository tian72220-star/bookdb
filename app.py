import os
from flask import Flask, request, redirect, render_template, url_for, session
from database import (init_db, add_book, list_books, delete_book_by_id,
                      update_book_by_id, search_books, get_book_by_id, 
                      get_stats, add_user, find_user, check_user)

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-12345'

init_db()

# 创建默认管理员（第一次运行）
try:
    add_user('admin', 'admin123', is_admin=1)
except:
    pass  # 已存在则跳过

def require_login(f):
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/')
def index():
    keyword = request.args.get('keyword', '').strip()
    rows = search_books(keyword) if keyword else list_books()
    total, latest = get_stats()
    user = None
    if session.get('user_id'):
        user = {'id': session['user_id'], 'username': session['username'], 
                'is_admin': session.get('is_admin', 0)}
    return render_template('index.html', books=rows, keyword=keyword,
                           total=total, latest=latest, user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if find_user(username):
            error = 'Username already exists'
        else:
            add_user(username, password)
            return redirect(url_for('login_page'))
    return render_template('register.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = check_user(username, password)
        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['is_admin'] = user[3]
            return redirect(url_for('index'))
        else:
            error = 'Wrong username or password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
@require_login
def add():
    add_book(request.form['title'],
             request.form['author'],
             request.form['publish_date'],
             request.form['isbn'])
    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>')
@require_login
def delete(book_id):
    delete_book_by_id(book_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:book_id>')
@require_login
def edit_page(book_id):
    book = get_book_by_id(book_id)
    return render_template('edit.html', book=book)

@app.route('/update/<int:book_id>', methods=['POST'])
@require_login
def update(book_id):
    update_book_by_id(book_id,
                      request.form['title'],
                      request.form['author'],
                      request.form['publish_date'],
                      request.form['isbn'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))