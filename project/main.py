from fastapi import FastAPI
from typing import Dict

app = FastAPI()
# tworzymy obiekt, z tego co zaimportowalismy
# bardzo wazny obiekt, rdzen projektu


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
# testowanie czy wyswietla cos

# tu okreslamy rooting naszej aplikacji, nasze kontrolery/endpointy
# get lub post - jaka metoda protokolu http ma byc tu wykorzystywana

# @app.get("/ships")
# async def index():
#     return {"message": "List of ships"}

# index - jak lista
# get - pobranie 1
# delete - usuwa


@app.post("/ships")
async def get():
    return {"message": "Add new ship"}



# @app.get("/ships/{ship_id}")
# async def get(ship_id: int) -> dict:
#     return {"message", f"Getting ship with id {ship_id}"}
# # nie może byc tu przecinek(a dwukropek), bo nie zgadzaja sie typy- zamiast dict tworzy sie set

# ladniej:
# @app.get("/ships/{ship_id}")
# async def get(ship_id: int) -> Dict[str, str]:
#     return {"message": f"Getting ship with id {ship_id}"}

# aby wejsc i to przejrzec:
# http://localhost:8000/ships
# http://localhost:8000/docs

# odbieranie danych od uzytkownika:
@app.get("/ships/{ship_id}")
async def get(ship_id):
    return {"message", f"Getting ship with id {ship_id}"}

# nie zawsze te dane przekazywane w adresie musza byc podawane
# np paginacja - nr strony - dodajemy wartosc domyslna, zeby tej info nie rpzekazywac w url

@app.get("/ships")
async def index(page: int = 0):
    # wartoscia domyslna jest zero
    return{"message": f"list of ships, page number {page}"}
# gdyby bylo wiecej parametrow:
# http://127.0.0.1:8000/ships?page=1&drugiparametr=

# zeby przekazac cos wiekszego: nie uzywamy adresu url
# zwlaszcza jezeli chcemy zapisac dane w naszym serwerze, bazie danych
