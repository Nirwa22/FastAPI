from fastapi import FastAPI
app = FastAPI()

inventory = {
    1: {
        "name": "Regular_milk",
        "price": "$3.99",
        "Amount": "2Litres"}
}


@app.get("/get/{item_id}")
def get(item_id: int):
    return inventory[item_id]
