from flask_restplus import Namespace, Resource

api = Namespace('test', description='teste teste')


@api.route('')
class Test(Resource):
    @api.doc('este é um teste de get')
    def get(self):
        return "teste"

    @api.doc('este é um teste de post')
    def post(self):
        return "test_post"