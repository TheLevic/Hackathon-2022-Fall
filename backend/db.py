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
            cursor.execute("CREATE TABLE person(name TEXT, images TEXT, song TEXT)")
    def createConn(self):
        conn = sqlite3.connect("database.db");
        return conn;


    def insertName(self, name: str,images,song):
        conn = self.createConn();
        cursor = conn.cursor();
        cursor.execute("""INSERT INTO person (name, images, song) values(?,?,?)""",(name,images, song));
        conn.commit();
        conn.close();

    def insertImages(self, images):
        pass;
    def insertSong(self, song: str):
        pass;

db = DB();
db.createDatabase();
db.insertName("other1", "other", "other");


