from flask_restful import Resource, reqparse
from index import api, db
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel
from modules.veterinario.domain.models.Vacuna import Vacuna


class Vacunas(Resource):
    def get(self):
        return parsemodel(Vacuna.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str)
        parser.add_argument('detalles', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["nombre", "detalles"])
        if not isValid:
            return None, 400
        nombre = args['nombre']
        detalles = args['detalles']
        vacuna = Vacuna(nombre=nombre, detalles=detalles)
        db.session.add(vacuna)
        db.session.commit()
        return vacuna.toJSON(), 201


def vacunas():
    api.add_resource(Vacunas, '/vacunas')
