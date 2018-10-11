from flask import Flask
from flask import render_template

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files/')
@app.route('/files/<path:file_path>')
def files(file_path=''):
    base_path = os.getcwd()
    return render_template('files.html',
        base_path=base_path,
        path=file_path,
    )
