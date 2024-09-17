import sys
from flask import Flask, Response
import time

app = Flask(__name__)

def generate_sse_data():
    """Generator that yields data every second."""
    while True:
        time.sleep(1)
        print("yield data")
        yield f"data: {int(time.time())} \n\n"  

@app.after_request
def disable_buffering(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route('/stream')
def stream():
    response = Response(generate_sse_data(), content_type='text/event-stream', 
                        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"})
    del response.headers['Content-Length']  
    return response

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
