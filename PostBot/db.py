import sqlite3

conn = sqlite3.connect(f'../db.sqlite3')
cursor = conn.cursor()
conn.commit()  # Commit change database


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    @property
    def get_ids_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM apps_facemodel").fetchall()

    @property
    def get_count(self):
        with self.connection:
            return self.cursor.execute("SELECT COUNT(*) FROM apps_facemodel;")

    @property
    def get_all_users(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM apps_facemodel").fetchall()


conn.close()  # Closing database connection
