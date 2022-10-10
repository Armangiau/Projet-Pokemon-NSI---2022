from flask import render_template
from random import randint
from controllers.Controller import Controller
from controllers.Controller import ControllerUtilities

from databaseUtilites import databaseUtilites


class ResultOfSearchController(Controller):

    def __init__(self, request: dict) -> None:
        self.request = request
        self.pokemonName = self.request['name']
        self.strRender =""

    def _getPokemonInfosAndNames(self) -> tuple[list, list]:
        database = databaseUtilites()
        pokemonInfos = database.Querry(
            'SELECT * FROM pokemons WHERE name=?', (self.pokemonName,))

        pokemonNames = database.Querry('SELECT name FROM pokemons') 
        database.close()

        return pokemonInfos, pokemonNames
        
    def _getPokemonInfos(self) -> list :
        database = databaseUtilites()
        pokemonInfos = database.Querry(
            'SELECT * FROM pokemons WHERE name=?', (self.pokemonName,))
        database.close()

        return pokemonInfos

    def newComponent(self) :
        pokemonInfos = self._getPokemonInfos()
        if pokemonInfos :
            self.strRender = render_template(
                "pokemonDescription.html", 
                pokemonInfos=ControllerUtilities.addPokemonsKeyInfo(pokemonInfos[0]),
                NameForImage=ControllerUtilities.formatPokemonNameForImages(pokemonInfos[0][1]),
                randcolor=randint(0, 360)
            )
        else :
            self.strRender = "Aucun Pokemon ne correspond à votre recherche : <a href='/' class='link link-secondary'>Retour à l'écran de recherche</a>"
        return self

    def newPage(self) :
        pokemonInfos, pokemonNames = self._getPokemonInfosAndNames()
        if pokemonInfos:
            self.strRender = render_template(
                "resultOfSearch.html",
                pokemonInfos=ControllerUtilities.addPokemonsKeyInfo(
                    pokemonInfos[0]),
                pokemonNames=pokemonNames,
                NameForImage=ControllerUtilities.formatPokemonNameForImages(
                    pokemonInfos[0][1]),
                randcolor=randint(0, 360)
            )
        else:
            self.strRender = render_template("noPokemonFound.html")
        return self

    def render(self) -> str:
        if not (self.strRender):
            return self.newPage().render()
        else:
            return self.strRender
