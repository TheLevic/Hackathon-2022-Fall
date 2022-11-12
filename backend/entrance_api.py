from flask import Flask, jsonify
from flask_cors import CORS
import db

Debug = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"./*":{'origins': '*'}})

if __name__ == "__main__":
    test = db.DB()
    test.createDatabase()
    app.run()