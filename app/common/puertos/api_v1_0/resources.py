from flask import request, Blueprint
from flask_restful import Resource, Api

from app.common.error_handling import ObjectNotFound

from .schemas import AstilleroSchema, DisenadorSchema, VeleroSchema
from ..models import Astillero, Disenador, Velero

puertos_v1_0_bp = Blueprint('puertos_v1_0', __name__)
api = Api(puertos_v1_0_bp)

astillero_schema = AstilleroSchema()
disenador_schema = DisenadorSchema()
velero_schema = VeleroSchema()

class AstilleroListResource(Resource):
    def get(self):
 
        astilleros = Astillero.get_all()
        return astillero_schema.dump(astilleros, many=True)

    def post(self):
 
        data = request.get_json()
        astillero_dict = astillero_schema.load(data)
        astillero = Astillero(**astillero_dict)
        astillero.save()
        return astillero_schema.dump(astillero), 201


class AstilleroResource(Resource):
    def get(self, id):
        astillero = Astillero.get_by_id(id)
        if astillero is None:
            raise ObjectNotFound("Astillero no encontrado")
        return astillero_schema.dump(astillero)

    def put(self, id):
        astillero = Astillero.get_by_id(id)
        if astillero is None:
            return {"message": "Astillero no encontrado"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(astillero, key, value)
        astillero.save()
        return astillero_schema.dump(astillero)

    def delete(self, id):
        astillero = Astillero.get_by_id(id)
        if astillero is None:
            raise ObjectNotFound("Astillero no encontrado")
        astillero.delete()
        return {"message": "Astillero eliminado"}, 204


class DisenadorListResource(Resource):
    def get(self):
        disenadores = Disenador.get_all()
        return disenador_schema.dump(disenadores, many=True)

    def post(self):
        data = request.get_json()
        disenador_dict = disenador_schema.load(data)
        disenador = Disenador(**disenador_dict)
        disenador.save()
        return disenador_schema.dump(disenador), 201
class DisenadorResource(Resource):
    def get(self, id):
        disenador = Disenador.get_by_id(id)
        if disenador is None:
            raise ObjectNotFound("Diseñador no encontrado")
        return disenador_schema.dump(disenador)

    def put(self, id):
        disenador = Disenador.get_by_id(id)
        if disenador is None:
            return {"message": "Diseñador no encontrado"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(disenador, key, value)
        disenador.save()
        return disenador_schema.dump(disenador)

    def delete(self, id):
        disenador = Disenador.get_by_id(id)
        if disenador is None:
            raise ObjectNotFound("Diseñador no encontrado")
        disenador.delete()
        return {"message": "Diseñador eliminado"}, 204


class VeleroListResource(Resource):
    def get(self):
        veleros = Velero.get_all()
        return velero_schema.dump(veleros, many=True)

    def post(self):
        data = request.get_json()
        velero_dict = velero_schema.load(data)
        velero = Velero(**velero_dict)
        velero.save()
        return velero_schema.dump(velero), 201
class VeleroResource(Resource):
    def get(self, id):
        velero = Velero.get_by_id(id)
        if velero is None:
            raise ObjectNotFound("Velero no encontrado")
        return velero_schema.dump(velero)

    def put(self, id):
        velero = Velero.get_by_id(id)
        if velero is None:
            return {"message": "Velero no encontrado"}, 404
        data = request.get_json()
        for key, value in data.items():
            setattr(velero, key, value)
        velero.save()
        return velero_schema.dump(velero)

    def delete(self, id):
        velero = Velero.get_by_id(id)
        if velero is None:
            raise ObjectNotFound("Velero no encontrado")
        velero.delete()
        return {"message": "Velero eliminado"}, 204



api.add_resource(AstilleroListResource, '/api/v1.0/astilleros/', endpoint='astilleros_list')
api.add_resource(AstilleroResource, '/api/v1.0/astilleros/<int:id>', endpoint='astillero_detail')
api.add_resource(DisenadorListResource, '/api/v1.0/disenadores/', endpoint='disenadores_list')
api.add_resource(VeleroListResource, '/api/v1.0/veleros/', endpoint='veleros_list')
api.add_resource(DisenadorResource, '/api/v1.0/disenadores/<int:id>', endpoint='disenador_detail')
api.add_resource(VeleroResource, '/api/v1.0/veleros/<int:id>', endpoint='velero_detail')