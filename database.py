import sqlite3
import time

class Database:
    def __init__(self, db_file_path) -> None:
        self.connection = sqlite3.connect(db_file_path)
        self.cursor = self.connection.cursor()
        #self.connection.row_factory = sqlite3.Row
        
    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
    
    def is_user_exists(self, user_id) -> bool:
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))
    
    def set_time_sub(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `time_sub` = ? WHERE `user_id` = ?",(time_sub, user_id))
    
    def get_user_id(self, user_id):
        return user_id
    
    def get_time_sub(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            return time_sub
        
    def get_request_sub(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `request_num` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                request_num = int(row[0])
            return request_num
    
    def get_user(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            aRes = dict()
            aRes["user_id"] = result[0][1]
            aRes["nickname"] = result[0][2]
            aRes["time_sub"] = result[0][3]
            aRes["request_num"] = result[0][4]
            return aRes
        
    def get_sub_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ?", (user_id)).fetchall()
            for row in result:
                time_sub = int(row[0])
            if time_sub > int (time.time()):
                return True
            else:
                return False