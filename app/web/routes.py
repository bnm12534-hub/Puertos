from flask import Blueprint, render_template, redirect, url_for, flash
from app.common.puertos.models import User
from app.forms import LoginForm
from app.db import db
web_bp = Blueprint('web', __name__)



@web_bp.route('/')
def index():
    return redirect(url_for('web.login'))
@web_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            flash('Login exitoso', 'success')
            return redirect(url_for('web.principal'))
        else:
            flash('Email o contraseña incorrectos', 'danger')
    return render_template('login.html', form=form)
@web_bp.route('/principal')
def principal():
    return render_template('principal.html')
@web_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email ya registrado', 'danger')
            return redirect(url_for('web.register'))
        new_user = User(email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registro exitoso, por favor inicia sesión', 'success')
        return redirect(url_for('web.login'))
    if form.errors:
        print(form.errors)
    return render_template('register.html', form=form)