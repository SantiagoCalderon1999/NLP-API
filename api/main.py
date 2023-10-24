from flask import jsonify, request, Flask
from routes.language_routes import language_routes

app = Flask(__name__)
app.register_blueprint(language_routes)

if __name__ == '__main__':
    app.run()