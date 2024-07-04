from flask import Flask, send_from_directory
import os

app = Flask(__name__)

react_folder = 'front'
directory = os.getcwd() + f'/{react_folder}/dist/assets'

@app.route('/')
def index():
    path = os.getcwd() + f'/{react_folder}/dist'
    print(path)
    return send_from_directory(directory=path, path='index.html')


@app.route('/front/<folder>/<file>')
def css(folder, file):
  path = folder + '/' + file
  return send_from_directory(directory=directory, path=file)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)