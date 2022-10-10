from camel_snake_kebab import kebab_case


class Controller:

    def __str__(self) -> str:
        return "A controlleur is used to prepare the data wich is used in the template(UI), it can also be connected with the database"

    def render(self) -> str:
        return "<html> <body> <h1> Render HTML in render() function <h1/> <body/> </html>"
    
    def asNewPage(self) -> str :
        pass


class ControllerUtilities:

    def formatPokemonNameForImages(name: str) -> str:
        finalStrName = kebab_case(name)
        return finalStrName

    def addPokemonsKeyInfo(pokemmonInfos: list) -> dict:
        PokemonsKeyInfo = ['id', 'name', 'type1', 'type2', 'total', 'hp', 'attack',
                           'defense', 'spAtk', 'spDef', 'speed', 'generation', 'legendary']
        return dict(zip(PokemonsKeyInfo, pokemmonInfos))
