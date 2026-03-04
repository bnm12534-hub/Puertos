from flask import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), email()])
    password = StringField('Password', validators=[DataRequired(), email()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Iniciar Sesión')