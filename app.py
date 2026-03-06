{\rtf1\ansi\ansicpg936\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
from flask import Flask, request, redirect, render_template, url_for\
from database import (init_db, add_book, list_books, delete_book,\
                      update_book, search_books)\
\
app = Flask(__name__)\
init_db()\
\
@app.route('/')\
def index():\
    keyword = request.args.get('keyword', '').strip()\
    if keyword:\
        rows = search_books(keyword)      # \uc0\u26377 \u25628 \u32034 \u35789  \u8594  \u27169 \u31946 \u25628 \u32034 \
    else:\
        rows = list_books()               # \uc0\u26080 \u25628 \u32034 \u35789  \u8594  \u26174 \u31034 \u20840 \u37096 \
    return render_template('index.html', books=rows, keyword=keyword)\
\
@app.route('/add', methods=['POST'])\
def add():\
    add_book(request.form['title'],\
             request.form['author'],\
             request.form['publish_date'],\
             request.form['isbn'])\
    return redirect(url_for('index'))\
\
@app.route('/delete/<title>')\
def delete(title):\
    delete_book(title)\
    return redirect(url_for('index'))\
\
@app.route('/update', methods=['POST'])\
def update():\
    update_book(request.form['old_title'],\
                request.form['new_title'],\
                request.form['new_author'],\
                request.form['new_publish_date'],\
                request.form['new_isbn'])\
    return redirect(url_for('index'))\
\
if __name__ == '__main__':\
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))}