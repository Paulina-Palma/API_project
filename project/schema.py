from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ShipSchema(BaseModel):
    name: str
#     mozna tez inne nazwy zmiennych podawac dalej + typy

@app.post("/ships")
async def add(item: ShipSchema):
    print(item)
    return {"message": "Add new ship"}


# zeby przekazac cos wiekszego: nie uzywamy adresu url
# zwlaszcza jezeli chcemy zapisac dane w naszym serwerze, bazie danych
# uzywamy wtedy schemy