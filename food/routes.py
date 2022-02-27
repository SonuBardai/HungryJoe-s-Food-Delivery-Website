from flask import (render_template, request, session, redirect, 
                )
from food.app import app, db
import json
import os
from food.models import Menu, Book

with open(os.path.join(app.root_path, 'food\\static\\config.json'), 'r') as f:
    params = json.load(f)["params"]

@app.route('/')
def home():
    return render_template('index.html', params = params)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'admin' in session and session['admin'] == params['admin-username']:
        return redirect('/dashboard')
    else: 
        if request.method == "POST":
            username = request.form.get('username')
            password = request.form.get('password')
            if username == params['admin-username'] and password == params['admin-password']:
                session['admin'] = username
                return redirect('/dashboard')
        else:
            return render_template('login.html', params = params)

@app.route('/logout')
def logout():
    session.pop('admin')
    return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html', params=params)

@app.route('/dashboard')
def dashboard():
    if 'admin' in session and session['admin'] == params['admin-username']:
        items = Menu().query.all()
        return render_template('dashboard.html', params = params, items = items)
    else:
        return redirect('/login')

@app.route('/menu')
def menu():
    items = Menu.query.all()
    return render_template('menu.html', params = params, items = items)

@app.route('/prod-view/<string:slug>')
def prodView(slug):
    item = Menu.query.filter_by(slug = slug).first()
    return render_template("prod-view.html", params=params, item=item)

@app.route('/edit/<string:slug>', methods=['GET', 'POST'])
def edit(slug):
    if 'admin' in session and session['admin'] == params['admin-username']:
        if request.method == 'POST':
            if slug=='0':
                name = request.form.get('name')
                description = request.form.get('description')
                price = request.form.get('price')
                img_loc = request.form.get('img_loc')
                item_slug = name.replace(' ', '-')
                item_slug = item_slug.lower()
                newItem = Menu(name=name, description=description, price=price, img_loc=img_loc, slug=item_slug)
                db.session.add(newItem)
                db.session.commit()
                return redirect('/menu')
            else:
                editItem = Menu.query.filter_by(slug = slug).first()
                editItem.name = request.form.get('name')
                editItem.description = request.form.get('description')
                editItem.price = request.form.get('price')
                editItem.img_loc = request.form.get('img_loc')
                item_slug = editItem.name.replace(' ', '-')
                item_slug = item_slug.lower()
                editItem.slug = item_slug
                db.session.commit()     
                return redirect('/menu')
        if slug=='0':
            item = {}
            slug = 0
        else: 
            item = Menu.query.filter_by(slug = slug).first()
            slug = item.slug
        return render_template('edit.html', params = params, item = item, slug=slug)
    else:
        return redirect('/login')

@app.route('/about')
def about():
    return render_template('about.html', params = params)

@app.route('/book', methods = ['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        persons = request.form.get('persons')
        date = request.form.get('date')
        booking = Book(name=name, phone=phone, email=email, persons=persons, date=date)
        db.session.add(booking)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('book.html', params = params)

#MENU: sno, Name, Desc, Price, Slug, Img