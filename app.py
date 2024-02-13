# put request

from fastapi import FastAPI, Request

app = FastAPI()

fruits = [
    {
        "id": 1,
        "name": "apple",
        "colour": "red",
        "calories": 52
    },
    {
        "id": 2,
        "name": "banana",
        "colour": "yellow",
        "calories": 89
    }
]

@app.get("/fruit")
def get_all_fruits():
    return fruits

@app.put("/fruit/{id}")
async def edit_fruit(id: int, request: Request):
    fruit_update = await request.json()

    for i in range(len(fruits)):
        if fruits[i]["id"] == id:
            fruits[i] = {**fruit_update, "id": id}
            break

    return fruit_update

# delete request

@app.delete("/fruit/{id}")
def delete_fruit(id: int):
    fruit_index = 0
    
    for i in range(len(fruits)):
        if fruits[i]["id"] == id:
            fruit_index = i
            break


    del fruits[fruit_index]

    return{
        "message:" : "delete successful"
    }
