from contextlib import closing

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

    def init_db(self):
        with closing(self.get_connection()) as db:
            with open("../db/banco.sql") as arquivo:
                db.cursor().executescript(arquivo.read())

            db.commit()

class ConnectionFactorySQLite:

    def get_connection(self):
        return sqlite3.connect('alura.db')

    def init_db(self):
        with closing(self.get_connection()) as db:
            with open("../db/banco.sql") as arquivo:
                db.cursor().executescript(arquivo.read())

            db.commit()