from flask import Flask, request
from controllers.SearchController import SearchController
from controllers.ResultOfSearchController import ResultOfSearchController
from controllers.CompareController import CompareController
from controllers.ResultOfPokemonTypesController import ResultOfPokemonTypesController

app = Flask(__name__)

@app.route("/")
@app.route("/search")
def searchRoute():
    return SearchController().render()

@app.route("/resultOfSearch", methods = ['GET'])
def resultOfSearch():
    if request.method == 'GET':
        return ResultOfSearchController(request.args).render()


@app.route("/compareName", methods = ['POST'])
def compareName():
    if request.method == 'POST':
        data = request.get_json()
        return ResultOfSearchController(data).newComponent().render()


@app.route("/resultTypeSearch", methods = ['POST'])
def resultOfTypeSearch():
    if request.method == 'POST':
        return ResultOfPokemonTypesController(request.form).render()


@app.route("/compareType", methods = ['POST'])
def compareType():
    if request.method == 'POST':
        data = request.get_json()
        return ResultOfPokemonTypesController(data).newComponent().render()