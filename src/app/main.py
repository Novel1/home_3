import fastapi
from pydantic import BaseModel
from typing import Union
from fastapi.encoders import jsonable_encoder

router = fastapi.APIRouter(prefix="/api")


@router.get("/get-hello/{name}")
async def get_hello(name: str = fastapi.Path(..., title="The name to greet")):
    return {'response': f'Hello {name}! Welcome to Python Plues!'}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

items = {
    "roo": {"name": "Roman", "price": 1000},
}


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):    
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


@router.post("/item")
async def create_item(item: Item):
    return item



app = fastapi.FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0")

