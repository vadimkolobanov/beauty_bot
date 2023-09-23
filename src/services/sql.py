import sqlite3
from pathlib import Path


class DataBase:

    def __init__(self, db_file: str | Path):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    async def add_user(self, user_id: int, username: str, name: str) -> None:
        with self.connect:
            self.cursor.execute("""INSERT INTO user (id, username, name) VALUES (?, ?, ?)""",
                                [user_id, username, name])

    async def check_user(self, user_id: int) -> bool:
        with self.connect:
            self.cursor.execute(f"SELECT * FROM user WHERE id = ?", (user_id,))
            result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

    async def add_specialist(self, user_id: int, name: str, specifications: str, text: str, photo: str) -> None:
        if await self.check_user(user_id):
            with self.connect:
                self.cursor.execute("""INSERT INTO specialist (id, name, specifications, text, photo) 
                VALUES (?, ?, ?, ?, ?)""", [user_id, name, specifications, text, photo])
