from flask import Flask
from main import *
import os

app=Flask(__name__)

@app.route("/")
def land():
    asyncio.run(main())
    return "OI"