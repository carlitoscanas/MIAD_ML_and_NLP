#!/usr/bin/python
from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from model_deploy import pred_movie_genre

app = Flask(__name__)

api = Api(
    app,
    version='1.0',
    title='Movie Genre Prediction API',
    description='Movie Genre Prediction API')

ns = api.namespace('predict',
     description='Movie Genre Classification')

parser = api.parser()

parser.add_argument(
    'Plot',
    type=str,
    required=True,
    help='Plot of the movie',
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class MovieGenreApi(Resource):
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        return {
         "result": pred_movie_genre(args['Plot'])
        }, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)