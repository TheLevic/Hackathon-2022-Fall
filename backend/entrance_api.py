from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import db
import os


Debug = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"./*":{'origins': '*'}})
name = ["Test", "Test2"];

def createDirectory(name):
    try:
        if (os.path.exists(f"../Images/{name}")):
            print("Directory already exists");
        else:
            os.mkdir(f'../Images/{name}');
    except:
        print("Error creating directory");

#Method to get our users name from the front end, make a directory, and then store it in our database
@app.route("/name", methods=["POST"])
def getName():
    content_type = request.headers['Content-Type'];
    if content_type == "application/json":
        data = request.json;
        name[0] = data['Name'];
        database = db.DB();
        database.createDatabase();
        database.insertName(name[0]);
        createDirectory(str(data['Name']));
    return Response("", status=200);

@app.route("/files", methods=["POST"])
def getUserData():
    data = request.files.getlist('image');
    for image in data:
        filename = image.filename;
        image.save(f'../Images/{name[0]}/{filename}');
    return Response("", status=200);
    
@app.route("/songName", methods=["POST"])
def getSongName():
    contentType = request.headers['Content-Type'];
    if contentType == "application/json":
        data = request.json;
        name[1] = data['Song']; 
        database = db.DB();
        database.createDatabase();
        database.updateSongName(name[0], name[1]);
        return Response("Got song", status=200);
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000);