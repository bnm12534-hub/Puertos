from flask import render_template, redirect, url_for, flash
from app.common.puertos.models import User
from app.forms import LoginForm
from app.db import db
from entrypoint import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            flash('Login exitoso')
            return redirect(url_for('principal'))
        else:
            flash('Email o contraseña incorrectos')
    return render_template('login.html', form=form)
@app.route('/principal')
def principal():
    return render_template('principal.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email ya registrado')
            return redirect(url_for('register'))
        new_user = User(email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registro exitoso, por favor inicia sesión')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)