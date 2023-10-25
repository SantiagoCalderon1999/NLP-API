from flask import Flask, Blueprint
from routes.language_routes import language_routes
from flask_restx import Api

app = Flask(__name__)

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Natural Language Processing API',
    version='1.0',
    description='API leveraging Natural Language Processing',
)

api.add_namespace(language_routes)

app.register_blueprint(blueprint)
if __name__ == '__main__':
    app.run()