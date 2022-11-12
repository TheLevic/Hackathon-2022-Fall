from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import db

Debug = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"./*":{'origins': '*'}})

@app.route("/handle", methods=["GET","POST"])
def handle():
    if request.method == "POST":
        post_data = request.get_json();
        print(post_data);
    # print(request.json)
    
    return Response("", status=200)

if __name__ == "__main__":
    # test = db.DB()
    # test.createDatabase()
    app.run();