from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="../bot-frontend/build")

@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory("../bot-frontend", "build/index.html")