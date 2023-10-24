
from flask import Flask
from flask import jsonify

app = Flask(__name__)
 
@app.route('/natural-language-processing/named-entity-recognition/analyze-text')
def analyze():
    raw_text="Colombia is full of beautiful landscapes"

    return jsonify(raw_text)
 
if __name__ == '__main__':
 
    app.run()