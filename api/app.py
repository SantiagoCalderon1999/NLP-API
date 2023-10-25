from flask import Flask
from routes.language_routes import blueprint as language_blueprint

app = Flask(__name__)
app.register_blueprint(language_blueprint)

if __name__ == '__main__':
    app.run()