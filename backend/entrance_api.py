from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import db
import os
import main



Debug = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"./*":{'origins': '*'}})



def createDirectory(name):
    os.mkdir(f'Images/{name}');



@app.route("/handle", methods=["GET","POST"])
def handle():
    if request.method == "POST":
        # Get the name
        userName = request.form['name']
        createDirectory(userName);

        # Getting the images
        post_data = request.files.getlist("image");
        for file in post_data:
            file.save("Images/" + userName + "/" + file.filename);
        personsFilePath = "Images/" + userName +"/";
        #Get the song
        songName = request.form['song']
        database = db.DB();
        database.createDatabase();
        database.insertName(userName,personsFilePath,songName);
        main.changed = not main.changed;
    return Response("", status=200)

if __name__ == "__main__":
    # test = db.DB()
    # test.createDatabase()
    app.run(host="0.0.0.0",port=3000);