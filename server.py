from typing import Any

import nest_asyncio
from fastapi import FastAPI
from langchain.pydantic_v1 import BaseModel
from langserve import add_routes

from chains.agent import agent_chain

nest_asyncio.apply()

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using LangChain's Runnable interfaces",
)


class Input(BaseModel):
    input: str


class Output(BaseModel):
    output: Any


add_routes(
    app,
    agent_chain.with_types(input_type=Input, output_type=Output).with_config(
        {"run_name": "agent"}
    ),
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, loop="asyncio")
