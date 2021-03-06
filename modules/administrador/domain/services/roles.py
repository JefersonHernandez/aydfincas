from flask_restful import Resource, reqparse
from index import api, db
from modules.administrador.domain.models.Rol import Rol
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Roles(Resource):
    def get(self):
        return parsemodel(Rol.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('clave', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["email", "clave"])
        if not isValid:
            return None, 400
        description = args['descripcion']
        rol = Rol(description=description)
        db.session.add(rol)
        db.session.commit()
        return rol.toJSON(), 201


def loadroles():
    api.add_resource(Roles, '/roles')
