from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import db
import os



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
        
        #Get the song
        songName = request.form['song']
        
        
    return Response("", status=200)

if __name__ == "__main__":
    # test = db.DB()
    # test.createDatabase()
    app.run();