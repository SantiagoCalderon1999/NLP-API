from flask import jsonify, request, Flask
from Controllers import NamedEntityRecognitionController

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def analsyze():
    text = request.json['text']
    return NamedEntityRecognitionController.analyze(text)
 
if __name__ == '__main__':
 
    app.run()