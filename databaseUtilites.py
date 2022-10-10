import sqlite3
from sqlite3 import Connection, Cursor

class databaseUtilites :

  sqliteErr = sqlite3.Error

  defaultpokemondb = 'pokemon.db'

  def __init__(self, DBPath: str = defaultpokemondb) :
    self.DBPath = DBPath
    self.DBConnection = sqlite3.connect(self.DBPath)

  def createCursor(self) -> Cursor :
    cursor = self.DBConnection.cursor()
    return cursor

  def createDBConect(self) -> Connection :
    return self.DBConnection

  def close(self) -> None :
    if self.DBConnection:
        self.DBConnection.close()

  def Querry(self, command: str, variables: tuple[str] = ()) -> list | sqlite3.Error :
    try :
      cursor = self.createCursor()
      cursor.execute(command, variables)
      return cursor.fetchall()
    except self.sqliteErr as error:
      return error