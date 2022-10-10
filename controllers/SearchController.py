from flask import render_template
from controllers.Controller import Controller

from databaseUtilites import databaseUtilites

class SearchController(Controller) :

  def __init__ (self) :
    database =  databaseUtilites()
    self.pokemonNames = database.Querry('SELECT name FROM pokemons')
    database.close()

  def render(self) -> str :
    return render_template("searchPage.html", pokemons=self.pokemonNames)