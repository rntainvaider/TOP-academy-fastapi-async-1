import sqlite3
from typing import Any


def add_database() -> None:
    with sqlite3.connect("sqlite3.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS quote (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            author TEXT)""")
    connection.commit()
    connection.close()


def add_quote(text: str, author: str) -> None:
    with sqlite3.connect("sqlite3.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO quote (text, author)
                       VALUES (?, ?)""",
            (text, author),
        )
    connection.commit()
    connection.close()


def get_quote() -> list[Any]:
    with sqlite3.connect("sqlite3.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT text, author FROM quote""")
        return cursor.fetchall()


if __name__ == "__main__":
    add_database()
    print(get_quote())
