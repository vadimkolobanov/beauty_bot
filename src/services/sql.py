import sqlite3
from pathlib import Path
import json
import ast


class DataBase:

    def __init__(self, db_file: str | Path):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()
        self.cursor.row_factory = sqlite3.Row

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

    async def add_specialist(
            self,
            user_id: int,
            name: str,
            specifications: list,
            text: str | None,
            photo: str | None
    ) -> None:
        if await self.check_user(user_id):
            with self.connect:
                columns = ', '.join(['id', 'name'] + specifications + ['text', 'photo'])
                values = ', '.join([str(user_id), f"'{name}'"] + ["1" for i in range(len(specifications))] + [f"'{text}'", f"'{photo}'"])
                query = f"""INSERT INTO specialist ({columns}) VALUES ({values})"""
                self.cursor.execute(query)

    async def get_specialists(self, specification: str) -> list:
        with self.connect:
            query = f"""SELECT * FROM specialist WHERE {specification}=1"""
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            filtered_result = []
            for result in results:
                result = {column: result[column] for column in result.keys()
                          if result[column] is not None and result[column] != 0}
                filtered_result.append(result)
            return filtered_result

