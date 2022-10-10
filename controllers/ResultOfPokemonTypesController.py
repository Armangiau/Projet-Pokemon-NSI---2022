from flask import render_template
from random import randint
from controllers.Controller import Controller
from controllers.Controller import ControllerUtilities

from databaseUtilites import databaseUtilites


class ResultOfPokemonTypesController(Controller):

    def __init__(self, request: dict) -> None:
        self.strRender = ""
        self.request = request

    def _sqlWhere(self, request: dict, Definiedconstraints: dict) -> tuple[str, list]:
        finalWhereSql = ""
        finalArgsSql = []

        for requestKey in request:
            requestItem = request[requestKey]
            if requestItem and requestKey in Definiedconstraints.keys():
                sqlWhere = Definiedconstraints[requestKey]
                finalWhereSql += str(" " + sqlWhere)
                finalArgsSql.append(requestItem)
            elif requestKey == "legendaire" and requestItem == True or requestItem =="on":
                finalWhereSql += " AND legendary='True'"
        finalWhereSql = finalWhereSql.removeprefix(" AND ")
        return (finalWhereSql, finalArgsSql)

    def _getPokemonsInfos(self) -> list:

        Definiedconstraints = {
            "type1": "AND type1=?",
            "type2": "AND type2=?",
            "totalptsmin": "AND total>=?",
            "totalptsmax": "AND total<=?",
            "vieptsmin": "AND hp>=?",
            "vieptsmax": "AND hp<=?",
            "attaqueptsmin": "AND attack>=?",
            "attaqueptsmax": "AND attack<=?",
            "defenceptsmin": "AND defense>=?",
            "defenceptsmax": "AND defense<=?",
            "attaquespemin": "AND SpAtk>=?",
            "attaquespemax": "AND SpAtk<=?",
            "defencespemin": "AND SpDef>=?",
            "defencespemax": "AND SpDef<=?",
            "vitessemin": "AND speed>=?",
            "vitessemax": "AND speed<=?",
            "generation": "AND generation=?",
        }

        where, args = self._sqlWhere(self.request, Definiedconstraints)
        print(where, args)
        try:
            database = databaseUtilites()
            pokemonsInfos = database.Querry(
                f'SELECT * FROM pokemons WHERE {where}', tuple(args))
            database.close()
            return pokemonsInfos
        except:
            return "error connection at db"

    def _prerenderPokemonsDescriptions(self, pokemonsInfos: list) -> str:
        PokemonsDescriptions = []

        for pokemonInfos in pokemonsInfos:
            print(ControllerUtilities.addPokemonsKeyInfo(
                pokemonInfos))
            PokemonsDescriptions.append(
                render_template(
                    "pokemonDescription.html",
                    pokemonInfos=ControllerUtilities.addPokemonsKeyInfo(
                        pokemonInfos),
                    NameForImage=ControllerUtilities.formatPokemonNameForImages(
                        pokemonInfos[1]),
                    randcolor=randint(0, 360)
                )
            )
        return PokemonsDescriptions

    def Template(self, templatePath: str) -> str:
        pokemonsInfos = self._getPokemonsInfos()
        if pokemonsInfos:
            PokemonsDescriptions = self._prerenderPokemonsDescriptions(
                list(pokemonsInfos))
            template = render_template(
                templatePath,
                PokemonsDescriptions=PokemonsDescriptions,
                # keep only names of pokemons
                selectedPokemonsNames=map(lambda item: item[1], pokemonsInfos),
                zip=zip
            )
            return template
        else:
            return render_template("noPokemonFound.html")

    def newPage(self):
        self.strRender = self.Template("resultOfTypeSearchPage.html")
        return self

    def newComponent(self):
        self.strRender = self.Template("resultOfTypeSearchComp.html")
        return self

    def render(self) -> str:
        if not (self.strRender):
            return self.newPage().render()
        else:
            return self.strRender
