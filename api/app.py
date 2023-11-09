from flask import Flask, Blueprint
import flask
from routes.ner_routes import namespace as named_entity_recognition_namespace
from routes.lemmatization_routes import namespace as lemmatization_namespace
from flask_restx import Api

app = Flask(__name__)
flask.json.provider.DefaultJSONProvider.sort_keys = False

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Natural Language Processing API',
    version='1.0',
    description='API leveraging Natural Language Processing',
)

api.add_namespace(named_entity_recognition_namespace)
api.add_namespace(lemmatization_namespace)

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run()