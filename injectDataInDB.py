from csvDecoder import csvToDictByLine
from databaseUtilites import databaseUtilites

database = databaseUtilites()


def removeIndex(Decodedcsv: list) -> list:
    for line in Decodedcsv:
        del line["\ufeff#"]
    return Decodedcsv


try:
    cursor, sqliteConnection = database.createCursor(), database.createDBConect()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pokemons(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name VARCHAR(90),
        type1 VARCHAR(90),
        type2 VARCHAR(90),
        total SMALLINT,
        hp SMALLINT,
        attack SMALLINT,
        defense SMALLINT,
        spAtk SMALLINT,
        spDef SMALLINT,
        speed SMALLINT,
        generation SMALLINT,
        legendary BOOLEAN
    )''')

    csvContent = csvToDictByLine('pokemon.csv')
    csvContent = removeIndex(csvContent)
    print(csvContent)

    cursor.executemany("INSERT INTO pokemons (name, type1, type2, total, hp, attack, defense, spAtk, spDef, speed, generation, legendary) VALUES (:Name, :Type1, :Type2, :Total, :HP, :Attack, :Defense, :SpAtk, :SpDef, :Speed, :Generation, :Legendary)", csvContent)

    sqliteConnection.commit()
    cursor.close()

except database.sqliteErr as error:
    print('Error occured - ', error)
finally:
    database.close()
