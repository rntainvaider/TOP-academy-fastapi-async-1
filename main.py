from typing import Any

import httpx
from fastapi import FastAPI

from database import add_database, add_quote, get_quote

app = FastAPI()

QUOTE_API_URL = "https://api.quotable.io/random"

add_database()


@app.get("/random_quote/")
async def get_random_quote() -> dict[str, Any]:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(QUOTE_API_URL)
        data = response.json()
        return {"content": data["content"], "author": data["author"]}


@app.post("/save_quote/")
async def post_random_quote() -> dict[str, Any]:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get("http://127.0.0.1:8000/random_quote/")
        data = response.json()
        add_quote(data["content"], data["author"])
        return {"content": data["content"], "author": data["author"]}


@app.get("/get_quote/")
async def get_databse_quote() -> list[dict[str, Any]]:
    quote = get_quote()
    return [{"content": quot[0], "author": quot[1]} for quot in quote]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
