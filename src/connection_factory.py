import MySQLdb
import sqlite3


class ConnectionFactoryMysql:

    def get_connection(self):
        # tratamento de erro omitido
        return MySQLdb.connect(
            host="localhost",
            user='root',
            passwd='',
            db='alura'
        )

    def init_db(self, connection):
        with open("../db/banco.sql") as arquivo:
            connection.cursor().executescript(arquivo.read())

        connection.commit()


class ConnectionFactorySQLite:

    def get_connection(self):
        connection = sqlite3.connect(":memory:")
        self.init_db(connection)
        return connection

    def init_db(self, connection):
        with open("../db/banco.sql", mode="r", encoding="utf-8") as arquivo:
            connection.cursor().executescript(arquivo.read())
        connection.commit()
