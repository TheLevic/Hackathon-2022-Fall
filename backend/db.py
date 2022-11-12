import sqlite3
import os

class DB():
    def __init__(self):
        pass;
    def createDatabase(self):
        if (os.path.exists("database.db")):
            print("Exists")
        else:
            conn = sqlite3.connect("database.db");
            cursor = conn.cursor();
            cursor.execute("CREATE TABLE person(name TEXT, images BLOB, song TEXT)")
    def insertName(self, name: str):
        pass;
    def insertImages(self, images):
        pass;
    def insertSong(self, song: str):
        pass;

    


