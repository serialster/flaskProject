from json import loads
from dicttoxml import dicttoxml
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


@app.route('/api/main', methods=['GET'])
class Main(Resource):
    def get(self):
        json_data = request.get_json()
        xml = dicttoxml(json_data)
        return xml

api.add_resource(Main, '/api/main')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')

