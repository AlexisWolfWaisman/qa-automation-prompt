import sqlite3

class Db_connection:
    def __init__(self, db_name="request_logs.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def insert_record(self, url, name_parameter, response_status, response_text):
        query = """
        INSERT INTO request_logs (url, name_parameter, response_status, response_text)
        VALUES (?, ?, ?, ?)
        """
        self.cursor.execute(query, (url, name_parameter, response_status, response_text))
        self.connection.commit()

    def delete_record(self, log_id):
        query = "DELETE FROM request_logs WHERE id = ?"
        self.cursor.execute(query, (log_id,))
        self.connection.commit()

    def update_record(self, log_id, url=None, name_parameter=None, response_status=None, response_text=None):
        query = "UPDATE request_logs SET "
        params = []
        if url:
            query += "url = ?, "
            params.append(url)
        if name_parameter:
            query += "name_parameter = ?, "
            params.append(name_parameter)
        if response_status:
            query += "response_status = ?, "
            params.append(response_status)
        if response_text:
            query += "response_text = ?, "
            params.append(response_text)
        query = query.rstrip(", ") + " WHERE id = ?"
        params.append(log_id)
        self.cursor.execute(query, params)
        self.connection.commit()   
   
        query = "SELECT * FROM request_logs"
        self.cursor.execute(query)
        return self.cursor.fetchall()  
    
    def count_OK_records(self):
        query = "SELECT COUNT(*) FROM request_logs WHERE response_status = 200"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
    
    def count_records(self):
        query = "SELECT COUNT(*) FROM request_logs"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]  
    
    def select_uptime_analisis(self):
        query = "SELECT response_status,timestamp FROM request_logs "
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def reset_table(self):
        query = "DELETE FROM request_logs"
        query2 = "DELETE FROM sqlite_sequence WHERE name='request_logs'"
        self.cursor.execute(query)
        self.cursor.execute(query2)
        self.connection.commit()

    def close(self):
        self.connection.close()    