from flask import Flask
from flask import request, render_template, redirect, send_file, safe_join

import os

from server import files

app = Flask(__name__)

@app.context_processor
def main_processor():
    return {
        'nav': [
            ('Index', 'r_index'),
            ('Files', 'r_files'),
        ],
    }

@app.route('/')
def r_index():
    return render_template('index.html')

@app.route('/files/')
@app.route('/files/<path:file_path>')
def r_files(file_path=''):
    base_path = os.getcwd()
    full_path = safe_join(base_path, file_path)
    status = 404

    # add trailing stash for directories
    if file_path and file_path[-1] != '/' and os.path.isdir(full_path):
        return redirect(request.path + '/', 302)

    # read path
    entry, entries = files.read_path(full_path)
    if entry:
        status = 200
        if not entry['is_dir'] and request.args.get('dl'):
            return send_file(full_path)

    return render_template('files.html',
        base_path=base_path,
        path=file_path,
        not_found=(status == 404),
        entry=entry,
        entries=entries,
    ), status
