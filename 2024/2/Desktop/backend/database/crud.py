import mysql.connector

class CRUD:
    def __init__(self, db):
        self.db = db
        self.cursor = None # cursor permite subir querys sql diretamente para o banco de dados

    def create(self, table, data):
        placeholders = ", ".join(["%s"] * len(data))
        columns = ", ".join(data.keys())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"  # placeholders adiciona "%" na string
        try:
            self.cursor = self.db.cnx.cursor()
            self.cursor.execute(query, tuple(data.values()))
            self.db.cnx.commit()
            print("Record successfully inserted.")
        except mysql.connector.Error as err:
            print(f"Error inserting record: {err}")

    def read(self, table, condition=None):
        query = f"SELECT * FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        try:
            self.cursor = self.db.cnx.cursor(dictionary=True)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error reading records: {err}")

    def update(self, table, updates, condition):
        update_string = ", ".join([f"{col} = %s" for col in updates.keys()])
        query = f"UPDATE {table} SET {update_string} WHERE {condition}"
        try:
            self.cursor = self.db.cnx.cursor()
            self.cursor.execute(query, tuple(updates.values()))
            self.db.cnx.commit()
            print("Record successfully updated.")
        except mysql.connector.Error as err:
            print(f"Error updating record: {err}")

    def delete(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        try:
            self.cursor = self.db.cnx.cursor()
            self.cursor.execute(query)
            self.db.cnx.commit()
            print("Record successfully deleted.")
        except mysql.connector.Error as err:
            print(f"Error deleting record: {err}")

    def close_cursor(self):
        if self.cursor:
            self.cursor.close()