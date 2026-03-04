from marshmallow import fields
from app.ext import ma
class AstilleroSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    pais = fields.Str()
    ciudad = fields.Str()
    año_fundacion = fields.Int()
    veleros = fields.Nested('VeleroSchema', many=True, exclude=('astillero',))
class DisenadorSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    nacionalidad = fields.Str()
    año_nacimiento = fields.Int()
    veleros = fields.Nested('VeleroSchema', many=True, exclude=('disenador',))
class VeleroSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    eslora = fields.Float()
    manga = fields.Float()
    calado = fields.Float()
    ano_fabricacion = fields.Int()
    astillero_id = fields.Int(load_only=True)
    disennador_id = fields.Int(load_only=True)
    astillero = fields.Nested(AstilleroSchema, only=('id', 'nombre'))
    disenador = fields.Nested(DisenadorSchema, only=('id', 'nombre'))