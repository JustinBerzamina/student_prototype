import sqlite3
from pathlib import Path


class Database:
    def __init__(self, database_path: str | Path = "school.db"):
        self.database_path = Path(database_path)
        self._connection: sqlite3.Connection | None = None

    def connect(self) -> sqlite3.Connection:
        if self.database_path == Path(":memory:"):
            if self._connection is None:
                self._connection = sqlite3.connect(self.database_path)
            return self._connection
        return sqlite3.connect(self.database_path)

    def create_table(self) -> None:
        with self.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
                """
            )

