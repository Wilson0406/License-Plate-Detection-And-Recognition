from flask import Flask, render_template, flash, request
import joblib as joblib
import os
import requests
import json
import base64
from main import num,plate

app = Flask(__name__)
#app = Flask(__name__, template_folder='foldername')
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def homepage():
    return render_template('index.html',value=plate)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
