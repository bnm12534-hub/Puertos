from app.db import db, BaseModelMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)
    def set_password(self, password):
        self.password=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
class Astillero(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(50))
    ciudad = db.Column(db.String(50))
    año_fundacion = db.Column(db.Integer)
    veleros = db.relationship('Velero', backref='astillero', lazy=True, cascade='all, delete-orphan')

    def __init__(self, nombre, pais, ciudad, año_fundacion, veleros=[]):
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.año_fundacion = año_fundacion
        self.veleros = veleros
    
    def __repr__(self):
        return f'Astillero({self.nombre})'
    def __str__(self):
        return f'Astillero: {self.nombre}, País: {self.pais}, Ciudad: {self.ciudad}, Año de Fundación: {self.año_fundacion}'

class Disenador(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    nacionalidad = db.Column(db.String(50))
    año_nacimiento = db.Column(db.Integer)
    veleros = db.relationship('Velero', backref='disenador', lazy=True, cascade='all, delete-orphan')
    def __init__(self, nombre, nacionalidad, año_nacimiento, veleros=[]):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.año_nacimiento = año_nacimiento
        self.veleros = veleros
    def __repr__(self):
        return f'Diseñador({self.nombre})'
    def __str__(self):
        return f'Diseñador: {self.nombre}, Nacionalidad: {self.nacionalidad}, Año de Nacimiento: {self.año_nacimiento}'
    
class Velero(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    eslora = db.Column(db.Float)
    manga = db.Column(db.Float)
    calado = db.Column(db.Float)
    ano_fabricacion = db.Column(db.Integer)
    astillero_id = db.Column(db.Integer, db.ForeignKey('astillero.id'))
    disennador_id = db.Column(db.Integer, db.ForeignKey('disenador.id'))
    def __init__(self, nombre, eslora, manga, calado, ano_fabricacion, astillero_id, disennador_id):
        self.nombre = nombre
        self.eslora = eslora
        self.manga = manga
        self.calado = calado
        self.ano_fabricacion = ano_fabricacion
        self.astillero_id = astillero_id
        self.disennador_id = disennador_id
    def __repr__(self):
        return f'Velero({self.nombre})'
    def __str__(self):
        return f'Velero: {self.nombre}, Eslora: {self.eslora}m, Manga: {self.manga}m, Calado: {self.calado}m, Año de Fabricación: {self.ano_fabricacion}'
    