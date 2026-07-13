import os
import sys

from fastapi import FastAPI

app = FastAPI()

try:
    secret_data1 = os.environ["SECRET1"]
    secret_data2 = os.environ["SECRET2"]
    env_data1 = os.environ["ENV1"]
    env_data2 = os.environ["ENV2"]
except KeyError as e:
    sys.exit(f"Missing env! {e}")


@app.get("/")
async def root():
    return {
        "message": "hello :)",
        "s1": secret_data1,
        "s2": secret_data2,
        "e1": env_data1,
        "e2": env_data2,
    }
