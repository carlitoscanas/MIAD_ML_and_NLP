#!/usr/bin/python
from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from xx_model_deployment import pred_car_price
#from model_deployment.xx_model_deployment import pred_car_price

app = Flask(__name__)

api = Api(
    app,
    version='1.0',
    title='Car Price Prediction API',
    description='Car Price Prediction API')

ns = api.namespace('predict',
     description='Car Price Regressor')

parser = api.parser()

parser.add_argument(
    'Year',
    type=float,
    required=True,
    help='Year of the car',
    location='args')

parser.add_argument(
    'Mileage',
    type=float,
    required=True,
    help='Mileage of the car',
    location='args')

parser.add_argument(
    'State',
    type=float,
    required=True,
    help='State of the car',
    location='args')

parser.add_argument(
    'Make',
    type=float,
    required=True,
    help='Make of the car',
    location='args')

parser.add_argument(
    'Model',
    type=float,
    required=True,
    help='Model of the car',
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.Float,
})

@ns.route('/')
class CarPriceApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()

        return {
         "result": pred_car_price(args['Year'],args['Mileage'],args['Make'],args['Make'],args['Model'])
        }, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)