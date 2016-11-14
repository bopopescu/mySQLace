""" MySQLace - Python interface for MySQL connections.
Copyright (C) 2016  Jordan Yerandi Cortes Guzman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from constants import CONN_STATUS
import mysql.connector

class mySQLace:
    def connect(self, username, passwd=None, host="127.0.0.1", dbName=None, port=21, socket=None):
        config = {
            'user': username,
            'password': passwd,
            'host': host,
            'database': dbName,
            'raise_on_warnings': True,
        }

        try:
            self.cnx = mysql.connector.connect(**config)

            self.status = CONN_STATUS.CONNECTED
        except mysql.connector.Error as err:
            self.status = CONN_STATUS.FAILED
            self.status_msg = err
        else:
            self.cnx.close()

    def disconnect(self):
        self.cnx.close()
        self.status = CONN_STATUS.READY

    def __init__(self):
        self.status = CONN_STATUS.READY
