import sqlite3
import os

class DB():
    def __init__(self):
        pass;
    def createDatabase(self):
        if (os.path.exists("database.db")):
            print("Database already exists");
        else:
            conn = sqlite3.connect("database.db");
            cursor = conn.cursor();
            cursor.execute("CREATE TABLE person(name TEXT, songname TEXT)")
            conn.commit();
            conn.close();
    def createConn(self):
        conn = sqlite3.connect("database.db");
        return conn;

    # Create method to just insert the name into the database
    def insertName(self, name: str):
        conn = self.createConn();
        cursor = conn.cursor();
        cursor.execute("INSERT INTO person VALUES(?, ?)", (name, ""));
        conn.commit();
        conn.close();

    # Update the songname for a user in the database
    def updateSongName(self, name: str, songname: str):
        conn = self.createConn();
        cursor = conn.cursor();
        cursor.execute("UPDATE person SET songname = ? WHERE name = ?", (songname, name));
        conn.commit();
        conn.close();