import sqlite3
from typing import Dict


class Db:
    def __init__(self, db_name: str, table: str, column: Dict):
        self.db_name = db_name or 'temp.db'
        self.conn = sqlite3.connect(self.db_name)  # создание соединения
        self.cur = self.conn.cursor()  # для запросов
        self.table = table
        self.column = ', '.join(f'{key} {column[key]}' for key in column)
        self.mask = ', '.join('?' for _ in range(len(column)))
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table}({self.column});")
        self.conn.commit()

    def write_one(self, value):
        self.cur.execute(f"INSERT INTO {self.table} VALUES({self.mask});", value)
        self.conn.commit()

    def write_many(self, more_value):
        self.cur.executemany(f"INSERT INTO {self.table} VALUES({self.mask});", more_value)
        self.conn.commit()

    def fetch_several(self, count):
        self.cur.execute(f"SELECT * FROM {self.table};")
        return self.cur.fetchmany(count)

    def fetch_all(self):
        self.cur.execute(f"SELECT * FROM {self.table};")
        return self.cur.fetchall()

    def delete(self, column_name, value):
        self.cur.execute(f"DELETE FROM {self.table} WHERE {column_name}='{value}';")
        self.conn.commit()


# db = Db('tmp', 'tbl', {'name': 'TEXT', 'age': 'INT'})

# value = ('18', 'Alex')
# db.write_one(value)
# value = ('Bob', '36')
# db.write_one(value)
# more_users = [('Peter', '00003'), ('Bruce', '00004')]
# print(db.fetch_several(3))
# print(db.fetch_all())
# db.delete('name', 'Bruce')

