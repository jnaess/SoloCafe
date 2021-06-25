from flask import Flask
from flask import request, render_template

from joblib import load
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

