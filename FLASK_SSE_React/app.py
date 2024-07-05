from datetime import datetime
import time

from flask import Flask, send_from_directory, Response, stream_with_context
import os

app = Flask(__name__)

react_folder = 'front'
directory = os.getcwd() + f'/{react_folder}/dist/assets'
# serve static files
@app.route('/')
def index():
    path = os.getcwd() + f'/{react_folder}/dist'
    print(path)
    return send_from_directory(directory=path, path='index.html')


@app.route('/front/<folder>/<file>')
def css(folder, file):
  path = folder + '/' + file
  return send_from_directory(directory=directory, path=file)


@app.route("/stream")
def stream():
    def get_data():
        while True:
            time.sleep(1)
            yield f'data: {datetime.now()}\n\n'

    return Response(stream_with_context(get_data()), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)