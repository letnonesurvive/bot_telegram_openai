import sqlite3

class Database:
    def __init__(self, db_file_path) -> None:
        self.connection = sqlite3.connect(db_file_path)
        self.cursor = self.connection.cursor()
        
    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
    
    def is_user_exists(self, user_id) -> bool:
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))
    
   #def set_nick