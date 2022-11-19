from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import db
import os


Debug = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"./*":{'origins': '*'}})
name = ["Test"];

def createDirectory(name):
    try:
        if (os.path.exists(f"../Images/{name}")):
            print("Directory already exists");
        else:
            os.mkdir(f'../Images/{name}');
    except:
        print("Error creating directory");


@app.route("/handle", methods=["GET","POST"])
def handle():
    if request.method == "POST":
        print(len(request.files.getlist('files')));
        # Get the names 
        songName = request.form['song']
        userName = request.form['name']
        print(songName, userName);
        createDirectory(userName);

        # Getting the filess
        if (len(request.files.getlist('files')) > 1):
            post_data = request.files.getlist('files');
            for file in post_data:
                file.save(f'../Images/{userName}/{file.filename}');
        elif (len(request.files.getlist('files')) == 1):
            file = request.files.getlist('files')[0];
            file.save(f'../Images/{userName}/{file.filename}');
        personsFilePath = "../Images/" + userName +"/";
        #Get the song
        database = db.DB();
        database.createDatabase();
#        database.insertName(userName,personsFilePath,songName);
    return Response("", status=200);

#Method to get our users name from the front end, make a directory, and then store it in our database
@app.route("/name", methods=["POST"])
def getName():
    content_type = request.headers['Content-Type'];
    if content_type == "application/json":
        data = request.json;
        name[0] = data['Name'];
        createDirectory(str(data['Name']));
    return Response("", status=200);

@app.route("/files", methods=["POST"])
def getUserData():
    data = request.files.getlist('image');
    for image in data:
        filename = image.filename;
        image.save(f'../Images/{name[0]}/{filename}');
    return Response("", status=200);
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000);