import sys
from flask import Flask, Response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, origins=["http://localhost:9000"])

def generate_sse_data():
    """Generator that yields data every second."""
    while True:
        time.sleep(3)
        print("yield data")
        yield f"data: {int(time.time())} \n\n"  

@app.route('/stream')
def stream():
    response = Response(generate_sse_data(), content_type='text/event-stream', status=200)
    del response.headers['Content-Length']  
    response.headers['Cache-Control'] = 'no-cache'
    return response

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
